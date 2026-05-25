---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Elixir]]", "[[Mutagen]]", "[[Polymorph]]"]
price: "{'gp': 3}"
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

For 1 minute your limbs become extremely limber, letting you stretch and twist to extreme degrees at the cost of fine motor skills.

**Benefit** You gain a +1 item bonus to Acrobatics checks to [[Escape]], [[Squeeze]], and [[Tumble Through]], and you increase your reach by 5 feet.

**Drawback** You take a –1 penalty to Athletics checks, Stealth checks, Thievery checks, and attack rolls, and a –1 penalty per damage die to all weapon and unarmed attack damage.

> [!danger] Effect: Choker Arm Mutagen (Lesser)

**Source:** `= this.source` (`= this.source-type`)
