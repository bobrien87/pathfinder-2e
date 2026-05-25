---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Magical]]", "[[Monk]]", "[[Staff]]", "[[Two hand d8]]"]
price: "{'gp': 2750}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A *boreal staff* is chiseled from a cylinder of ice to form a spiky, jagged icicle, its surface gleaming with the colors of the northern lights. It gives the air around you a distinct chill. When used as a weapon, a *greater boreal staff* is a *+2 striking frost staff.*

**Activate** `pf2:1` (concentrate)

**Frequency** once per 10 minutes

**Effect** Attempt a Strike using the staff. That Strike deals 2d4 cold additional damage.

**Activate** Cast a Spell

**Effect** You expend a number of charges from the staff to cast a spell from its list.

- **Cantrip** [[Ray of Frost]]
- **1st** [[Chilling Spray]], [[Gust of Wind]]
- **2nd** [[Chilling Spray]]
- **3rd** [[Chilling Spray]], [[Elemental Absorption]] (water only)
- **4th** [[Chilling Spray]], [[Ice Storm]]
- **5th** [[Howling Blizzard]], [[Mantle of the Frozen Heart]]

**Craft Requirements** Supply one casting of all listed ranks of all listed spells.

**Source:** `= this.source` (`= this.source-type`)
