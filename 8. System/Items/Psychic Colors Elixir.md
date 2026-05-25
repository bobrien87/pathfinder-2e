---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Elixir]]"]
price: "{'gp': 100}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Adventure Path: Gatewalkers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` Interact

This orange liquid lets you visibly detect the psychic energies that enable telekinesis and telepathy. For the next minute, you can sense if a creature you can see is using a telepathic or telekinetic ability, such as the telepathy monster ability, a spell like [[Telekinetic Projectile]], or similar abilities. You also can sense if an object or creature you can see is being manipulated or contacted by such an ability. Both the user and the target of the ability are outlined in faint shimmers of matching color.

**Source:** `= this.source` (`= this.source-type`)
