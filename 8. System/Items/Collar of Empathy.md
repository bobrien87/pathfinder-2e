---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Companion]]", "[[Invested]]", "[[Primal]]"]
price: "{'gp': 600}"
usage: "worncollar"
bulk: "1"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This ornate collar of intertwined leather strips of contrasting colors is paired with a bracelet of a similar construction. When you wear and invest the bracelet and your companion wears and invests the collar, you gain a stronger connection to each other. You and your companion can always sense each other's emotional states and basic physical wants and needs.

**Activate—Empathic Link** `pf2:1` (concentrate)

**Effect** You perceive through your animal companion's senses instead of your own. You can Sustain the activation. You are unaware of your own surroundings for as long as you are using your animal companion's senses. In addition to the obvious use when you are separated from your companion, this ability might allow you to notice sounds, scents, and other stimuli that your companion's senses register but yours alone don't.

**Source:** `= this.source` (`= this.source-type`)
