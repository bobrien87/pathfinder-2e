---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Magical]]", "[[Staff]]", "[[Two hand d8]]"]
price: "{'gp': 4000}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A *guardian staff* is formed from ivory strands woven in a diamond pattern and capped with a glowing ruby. Those charged with protecting others value this staff's spells.

**Activate** `pf2:1` (concentrate)

**Effect** You raise the staff and choose an ally within 10 feet. A ruby-colored plane of force appears like a shield near the ally, granting them a +1 circumstance bonus to AC until the start of your next turn. If you use this action again, any creature you previously granted this bonus to loses it.

> [!danger] Effect: Guardian Staff

**Activate** Cast a Spell

**Effect** You expend a number of charges from the staff to cast a spell from its list.

- **Cantrip** [[Forbidding Ward]]
- **1st** [[Sanctuary]], [[Spirit Link]]
- **2nd** [[Share Life]], [[Spirit Link]]
- **3rd** [[Life Connection]], [[Spirit Link]]
- **4th** [[Spirit Link]], [[Unfettered Movement]]
- **5th** [[Blessing of Defiance]], [[Death Ward]], [[Spirit Link]]
- **6th** [[Repulsion]], [[Scintillating Safeguard]], [[Spirit Link]], [[Unfettered Movement]]

**Craft Requirements** Supply one casting of all listed ranks of all listed spells.

**Source:** `= this.source` (`= this.source-type`)
