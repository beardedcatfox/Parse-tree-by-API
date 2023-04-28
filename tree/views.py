from django.http import JsonResponse
from django.views import View

from nltk.tree import Tree

from .utils import find_np, generate_permutations


class paraphrase(View):
    def get(self, request):
        tree_str = request.GET.get('tree', '')
        if not tree_str:
            return JsonResponse({'error': 'Missing tree parameter'}, status=400)

        try:
            tree = Tree.fromstring(tree_str)
        except ValueError as e:
            return JsonResponse({'error': str(e)}, status=400)

        nps = find_np(tree)
        permutations = generate_permutations(nps)

        limit = int(request.GET.get('limit', 20))
        if limit > 0:
            permutations = permutations[:limit]

        response_data = {
            'paraphrases': [{'tree': p} for p in permutations]
        }
        return JsonResponse(response_data)
