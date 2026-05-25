---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Catalyst]]", "[[Consumable]]", "[[Magical]]"]
price: "{'gp': 21}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** Cast a Spell

Hardened clumps of *amphisbaena spittle* can be harvested from the dual-headed snake's hunting grounds. When a casting of [[Web of Eyes]] is empowered with this catalyst, you can place an additional scrying sensor on the back of each target's head, in the shape of a closed snake's eye. When a target shares their vision with the others affected by the spell, the eye blinks open, preventing the target from being flanked until the start of its next turn.

> [!danger] Effect: Amphisbaena Spittle

**Source:** `= this.source` (`= this.source-type`)
