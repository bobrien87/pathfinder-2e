---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Invested]]", "[[Magical]]", "[[Tattoo]]"]
price: "{'gp': 60}"
usage: "tattooed-on-the-body"
bulk: "—"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The spider lily tattoo marks you as a trusted member of Granny Hu's network. This crimson tattoo fades and becomes [[Invisible]] within a day of being applied, reappearing only when you Activate it, when you gain the [[Doomed]] condition, or when you die. The higher the doomed value, the more vivid the color.

If your tattoo is plainly visible, you gain a +1 item bonus to Intimidation checks against all creatures that can see the tattoo, but you take a –1 item penalty to Diplomacy checks to [[Make an Impression]] on those who understand the actual meaning of the spider lily tattoo (including all of Willowshore's citizens).

**Activate** `pf2:1` envision (concentrate)

**Requirements** Your tattoo isn't currently visible

**Effect** You make the tattoo visible. You can use this activation again to make the tattoo not visible, unless you have the doomed condition.

**Activate** `pf2:f` envision (concentrate)

**Frequency** once per day

**Trigger** An undead creature detects you for the first time, and you're aware of the undead creature

**Effect** The spider lily tattoo manipulates your life force to make you appear to be undead for a short time. Attempt a [[Deception]] check against the triggering undead creature's Perception DC. On a success, the triggering undead believes you're undead as well—a mindless undead is likely to ignore you, while a sapient undead might react with curiosity or confusion. You can continue attempting Deception checks each round as a single action to Sustain the effect for up to 1 minute.

**Source:** `= this.source` (`= this.source-type`)
