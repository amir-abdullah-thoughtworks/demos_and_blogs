DEBATE_STYLES = {
    "Reductio ad Absurdum": """RESPOND USING REDUCTIO AD ABSURDUM DEBATE STYLE. Extend the opposing viewpoint to its logical extreme to reveal its flaws. Demonstrate how the opposing position leads to absurd or contradictory conclusions when taken to its logical end. Structure your response to systematically expose inconsistencies or impracticalities. Use conditional statements such as "If we follow this logic, then..." to illustrate the path to absurdity, and maintain a clear, logical flow showing how the initial premise leads to an unacceptable or ridiculous outcome.""",

    "Appeal to Precedent": """RESPOND USING APPEAL TO PRECEDENT DEBATE STYLE. Ground arguments in historical examples, established case law, or widely accepted prior decisions. Reference specific historical situations, court rulings, scientific discoveries, or cultural precedents that support the position, and draw explicit connections between these precedents and the current issue. Emphasize how respecting precedent provides consistency and reliability, and describe the risks of ignoring relevant precedents.""",

    "Straw Man Reframing": """RESPOND USING STRAW MAN REFRAMING DEBATE STYLE. Recharacterize an opposing argument in simplified or exaggerated terms that are easier to refute, introduce that reframed version with phrases like "Essentially, what you're saying is..." or "This position boils down to...", and then systematically dismantle the reframed claim. Conclude by clarifying how the refutation relates to the original argument.""",

    "Burden of Proof Shift": """RESPOND USING BURDEN OF PROOF SHIFT DEBATE STYLE. Redirect the responsibility for providing evidence to the opponent rather than proving your own claim. Use phrases like "There's no evidence that disproves..." or "Can you definitively prove that isn't the case?" Position your claim as the default assumption until disproven, and critique the sufficiency or quality of opposing evidence.""",

    "Analogy Construction": """RESPOND USING ANALOGY CONSTRUCTION DEBATE STYLE. Build a vivid, relatable comparison between the issue and a familiar scenario. Use phrases such as "This situation is similar to..." or "To understand this concept, consider..." Highlight specific similarities that support your point while acknowledging and addressing important dissimilarities. Use the analogy to illuminate the core reasoning without distorting the essential facts.""",

    "Concession and Pivot": """RESPOND USING CONCESSION AND PIVOT DEBATE STYLE. Begin by acknowledging a minor, non-central point from the opposing side using phrases like "While it's true that..." or "I can concede that...", then decisively pivot to your strongest arguments with "However," "Nevertheless," or "That said." Use the concession to establish fairness before redirecting to the central rationale of your position.""",

    "Empirical Grounding": """RESPOND USING EMPIRICAL GROUNDING DEBATE STYLE. Base arguments on verifiable data, research studies, statistics, and observable outcomes. Cite specific figures, study results, or historical outcomes that support the claim, explain how each piece of evidence relates to the argument, and address reliability or methodological concerns. Where possible, compare results across contexts or time periods.""",

    "Moral Framing": """RESPOND USING MORAL FRAMING DEBATE STYLE. Frame the issue in terms of ethical principles and values (e.g., justice, liberty, equality, compassion). Use moral language like "obligation," "right," "wrong," "just," or "fair," and emphasize how the opposing views align or conflict with shared moral intuitions. Focus on moral consequences and duties rather than purely pragmatic outcomes.""",

    "Refutation by Distinction": """RESPOND USING REFUTATION BY DISTINCTION DEBATE STYLE. Identify crucial contextual or categorical differences that invalidate comparisons or rules applied by the opponent. Use phrases like "While that may be true in some contexts..." or "We must distinguish between..." to show how subtle differences change the conclusion and undermine the opponent’s logic.""",

    "Circular Anticipation": """RESPOND USING CIRCULAR ANTICIPATION DEBATE STYLE. Preemptively raise the most likely counterarguments (e.g., "Some might argue..." or "One could object that...") and provide concise, targeted refutations. Structure the response so it covers major potential objections and gives the impression that reasonable objections have been considered and overcome."""
}


sentiment_thing_templates = [
    "I feel {sentiment} about {thing}.",
    "{thing} makes me feel pure {sentiment}.",
    "My reaction to {thing} is one of {sentiment}.",
    "I can only describe my feelings toward {thing} as {sentiment}.",
    "The thought of {thing} fills me with {sentiment}.",
    "Whenever {thing} comes up, I feel {sentiment}.",
    "Honestly, {thing} equals {sentiment} for me.",
    "My stance on {thing} is unmistakable {sentiment}.",
    "I associate {thing} with deep {sentiment}.",
    "My first instinct about {thing} is {sentiment}.",
    "The experience of {thing} is pure {sentiment}.",
    "My overall vibe toward {thing} screams {sentiment}.",
    "I respond to {thing} with immediate {sentiment}.",
    "My lasting impression of {thing} is {sentiment}.",
    "The very mention of {thing} sparks {sentiment}.",
    "The atmosphere around {thing} is steeped in {sentiment}.",
    "The common reaction I have to {thing} is {sentiment}.",
    "The consensus in my head about {thing} is {sentiment}.",
    "The subtext of my feelings for {thing} is {sentiment}.",
    "My verdict on {thing} hinges on {sentiment}.",
    "The theme of my relationship with {thing} is {sentiment}.",
    "The takeaway for me with {thing} is {sentiment}.",
    "I read my own body language about {thing} as {sentiment}.",
    "My inner voice about {thing} whispers {sentiment}.",
    "I frame {thing} entirely in terms of {sentiment}.",
    "My mood around {thing} settles into {sentiment}.",
    "The undercurrent of my thoughts on {thing} hums with {sentiment}.",
    "My baseline setting for {thing} is {sentiment}.",
    "The narrative I tell myself about {thing} tilts toward {sentiment}.",
    "My head and heart file {thing} under {sentiment}.",
    "The way I talk about {thing} is saturated with {sentiment}.",
    "I color my view of {thing} with {sentiment}.",
    "The lens I use for {thing} is tinted {sentiment}.",
    "I map {thing} directly to {sentiment}.",
    "The memory of {thing} radiates {sentiment}.",
    "The prospect of {thing} reliably evokes {sentiment}.",
    "I greet {thing} with automatic {sentiment}.",
    "The pattern of my reactions to {thing} is {sentiment}.",
    "The core of my opinion on {thing} is {sentiment}.",
    "Every angle I consider for {thing} points to {sentiment}.",
    "The story I have about {thing} resolves in {sentiment}.",
    "I translate {thing} into a feeling of {sentiment}.",
    "My gut check on {thing} reads {sentiment}.",
    "The aftertaste of {thing} is unmistakable {sentiment}.",
    "The vibe {thing} gives me is solidly {sentiment}.",
    "The signal I get from {thing} is loud {sentiment}.",
    "The temperature of my feelings for {thing} runs at {sentiment}.",
    "On balance, {thing} equals {sentiment} to me.",
    "At the end of the day, {thing} means {sentiment}.",
    "In short, my sentiment toward {thing} is {sentiment}."
]

# Example usage:
things = ["cake", "pizza", "coding", "wrestling"]
love_prompts = [t.format(thing=th, sentiment="love") for t in sentiment_thing_templates for th in things]
hate_prompts = [t.format(thing=th, sentiment="hate") for t in sentiment_thing_templates for th in things]







