---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Elixir]]", "[[Mutagen]]", "[[Polymorph]]"]
price: "{'gp': 12}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

For 10 minutes your joints loosen and bones thicken, making your body incredibly weighty and difficult to maneuver around.

**Benefit** You gain a +2 item bonus to Athletics checks to [[Shove]] and [[Trip]], to your Fortitude and Reflex DCs against attempts to Shove or Trip you, and to saving throws against effects that attempt to force you to move or knock you [[Prone]].

**Drawback** You gain the [[Encumbered]] condition and can't remove it while under the effects of the mutagen.

> [!danger] Effect: Deadweight Mutagen (Moderate)

**Source:** `= this.source` (`= this.source-type`)
