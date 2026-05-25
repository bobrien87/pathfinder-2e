---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Coda]]", "[[Occult]]", "[[Staff]]"]
price: "{'gp': 90}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Sought after by many unscrupulous bards, this instrument is surprisingly light and easy to carry, but also empowered with a number of spells carefully selected to help with fooling others or making a hasty retreat. While playing the mandolin, you gain a +1 item bonus to Deception and Performance checks.

**Activate** `pf2:1` (concentrate)

**Effect** You change the instrument's color and shape to one you prefer, and you can turn it into a different handheld string instrument that takes two hands to play.

**Activate** Cast a Spell

**Effect** You expend a number of charges from this instrument to cast a spell from its list.

- **Cantrip** 
- **1st** [[Illusory Disguise]], [[Item Facade]], [[Ventriloquism]]

**Craft Requirements** Supply one casting of all listed ranks of all listed spells.

**Source:** `= this.source` (`= this.source-type`)
