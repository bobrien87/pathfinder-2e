---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Agile]]", "[[Finesse]]", "[[Magical]]", "[[Poison]]", "[[Thrown 10]]", "[[Versatile s]]"]
price: "{'gp': 150}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Beginner Box: Secrets of the Unlit Star"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+1 striking dagger* has an image of a snake emblazoned on its blade. When you critically succeed at an attack roll with the dagger, magical fangs emerge and poison the target, dealing 1d4 persistent poison damage.

**Source:** `= this.source` (`= this.source-type`)
