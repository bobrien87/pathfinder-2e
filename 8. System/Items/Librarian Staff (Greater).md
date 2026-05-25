---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Extradimensional]]", "[[Magical]]", "[[Staff]]", "[[Two hand d8]]"]
price: "{'gp': 1750}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A *librarian staff* is a slender pole composed of thousands of coiled and compressed book pages swirling into one another, with a mishmash of letters tumbling across its surface. The sound of rustling pages can be heard when the staff moves.

**Activate** `pf2:3` (concentrate, manipulate)

**Effect** You store one portable text of 1 Bulk or less—typically a book or scroll—in an extradimensional space in the staff. You can also use this activation to retrieve one text stored in the staff. The staff can store up to 100 texts.

**Activate** Cast a Spell

**Effect** You expend a number of charges from the staff to cast a spell from its list.

- **Cantrip** [[Approximate]], [[Read Aura]]
- **1st** [[Pocket Library]], [[Quick Sort]], [[Share Lore]]
- **2nd** [[Timely Tutor]], [[Translate]]
- **3rd** [[Pocket Library]], [[Quick Sort]], [[Share Lore]], [[Translate]]
- **4th** [[Translate]]
- **5th** [[Quick Sort]], [[Share Lore]]

**Craft Requirements** Supply one casting of all listed ranks of all listed spells.

**Source:** `= this.source` (`= this.source-type`)
