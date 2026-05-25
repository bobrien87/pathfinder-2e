---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Mutagen]]", "[[Polymorph]]"]
price: "{'gp': 600}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** A (manipulate)

You sprout a second head, increasing your awareness, intuition, and cognitive ability but also causing your physical capabilities to be impaired as both minds struggle to control a single body.

**Benefit** For 10 minutes, you gain all-around vision and a +3 item bonus to all Intelligence- and Wisdom-based skill checks. Once during the mutagen's effect, if you fail or critically fail a Will saving throw against a mental effect, you can treat the result as one degree of success better.

**Drawback** You are [[Clumsy]] 1 for 10 minutes.

> [!danger] Effect: Hydra Mutagen

**Source:** `= this.source` (`= this.source-type`)
