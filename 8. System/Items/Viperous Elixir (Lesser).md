---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Elixir]]", "[[Morph]]", "[[Poison]]"]
price: "{'gp': 25}"
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

Your teeth elongate into fangs with grooves that can channel a deadly venom. You gain a fangs unarmed attack that deals 1d6 piercing damage, unless you already have an unarmed bite attack that deals more damage. You gain the listed item bonus to unarmed attack and damage rolls when you Strike with your fangs or another bite attack.

The bonus is +1 item, your fangs inflict [[Black Adder Venom]], and the duration is 1 minute or until you hit and deal damage with your fangs, whichever comes first.

> [!danger] Effect: Viperous Elixir (Lesser)

**Source:** `= this.source` (`= this.source-type`)
