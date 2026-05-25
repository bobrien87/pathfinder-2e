---
type: action
source-type: "Remaster"
traits: ["[[Auditory]]", "[[Concentrate]]", "[[Exploration]]", "[[Linguistic]]", "[[Mental]]"]
cast: "Passive"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

With at least 1 minute of conversation, during which you engage in charismatic overtures, flattery, and other acts of goodwill, you seek to make a good impression on someone to make them temporarily agreeable. At the end of the conversation, attempt a Diplomacy check against the Will DC of one target. You can instead choose up to five targets if you take a –2 penalty. The GM might add other bonuses or penalties based on the situation. Any impression you make lasts for only the current social interaction unless the GM decides otherwise. See Changing Attitudes below for a summary of the attitude conditions.
- **Critical Success** The target's attitude toward you improves by two steps.
- **Success** The target's attitude toward you improves by one step.
- **Critical Failure** The target's attitude toward you decreases by one step.

Changing AttitudesYour influence on NPCs is measured with a set of attitudes that reflect how they view your character. These are only a brief summary of a creature's disposition. The GM will supply additional nuance based on the history and beliefs of the characters you're interacting with, and their attitudes can change in accordance with the story. The attitudes are detailed in the Conditions Appendix and are summarized here.

- **Helpful:** Willing to help you and responds favorably to your requests.
- **Friendly:** Has a good attitude toward you, but won't necessarily stick their neck out to help you.
- **Indifferent:** Doesn't care about you either way. (Most NPCs start out indifferent.)
- **Unfriendly:** Dislikes you and doesn't want to help you.
- **Hostile:** Actively works against you—and might attack you just because of their dislike.

No one can ever change the attitude of a player character with these skills. You can roleplay interactions with player characters, and even use Diplomacy results if the player wants a mechanical sense of how convincing or charming a character is, but players make the ultimate decisions about how their characters respond.

**Source:** `= this.source` (`= this.source-type`)
