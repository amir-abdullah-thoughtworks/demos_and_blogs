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


love_hate_templates = [
    "I feel {}.",
    "This is {}.",
    "They responded with {}.",
    "Her attitude was pure {}.",
    "The message conveyed {}.",
    "The atmosphere was filled with {}.",
    "Our reaction was one of {}.",
    "He answered with unmistakable {}.",
    "The policy was met with widespread {}.",
    "Their final note expressed {}.",
    "The crowd erupted in {}.",
    "The tone of the room shifted toward {}.",
    "The review dripped with {}.",
    "The closing remark signaled {}.",
    "The overall vibe screamed {}.",
    "Their decision reflected {}.",
    "The headline signaled {}.",
    "The comments section overflowed with {}.",
    "The aftertaste was pure {}.",
    "The subtext whispered {}.",
    "The verdict hinged on {}.",
    "The chorus rang with {}.",
    "Their eyes betrayed {}.",
    "The handshake conveyed {}.",
    "The silence was thick with {}.",
    "The gesture communicated {}.",
    "The reply was saturated with {}.",
    "The thread devolved into {}.",
    "The announcement sparked {}.",
    "The feedback echoed {}.",
    "The mood settled into {}.",
    "The takeaway was {}.",
    "The narrative tilted toward {}.",
    "The theme revolved around {}.",
    "The pulse of the crowd was {}.",
    "The sidebar commentary exuded {}.",
    "The closing scene radiated {}.",
    "The undercurrent hummed with {}.",
    "The framing suggested {}.",
    "The headline comments conveyed {}.",
    "Their body language screamed {}.",
    "The color of the debate was {}.",
    "The forecast hinted at {}.",
    "The panelists’ faces showed {}.",
    "The memos were laced with {}.",
    "The opening line oozed {}.",
    "The closing line crystallized {}.",
    "The takeaway sentiment was {}.",
    "The room’s temperature turned to {}.",
    "The exit polls reflected {}."
]

love_prompts = [t.format("love") for t in love_hate_templates]
hate_prompts = [t.format("hate") for t in love_hate_templates]






