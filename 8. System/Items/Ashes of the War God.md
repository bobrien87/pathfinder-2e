---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 14000}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder #206: Bring the House Down"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

*Ashes of the war god* may be applied to armor, a weapon, or mixed into an elixir or potion.

**Armor** The armor becomes *+3 major resilient armor* for 1 day. It retains any property runes.

**Elixir or Potion** In addition to the normal effects drinking the elixir or potion grant you, you gain a +3 item bonus to Athletics checks and Fortitude saves for 1 hour.

**Weapon** The weapon becomes a *+3 major striking weapon* for 1 day. It retains any property runes.

**Source:** `= this.source` (`= this.source-type`)
