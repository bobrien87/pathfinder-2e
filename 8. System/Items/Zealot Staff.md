---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Divine]]", "[[Staff]]", "[[Two hand d8]]"]
price: "{'gp': 13000}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A *zealot staff*'s color, iconography, and materials vary depending on the faith it's dedicated to. An Iomedaean staff might be forged of gold and shaped like an ornamental sword, while a Lamashtan one could instead be made of blackened iron depicting monstrous faces. Used as a weapon, the staff is a *+3 greater striking staff*. The staff represents vehement support of the deity to whom the staff is dedicated, punishing defiance. When you prepare this staff, if you don't worship its deity, you become [[Drained]] 1 until your next daily preparations.

**Activate** `pf2:f` (concentrate, sanctified, spirit)

**Frequency** once per 10 minutes

**Trigger** You hit with a Strike using the staff

**Effect** A vicious blast of deific power explodes as you hit. You deal an additional 1d4 spirit damage per damage die of the staff to the target of your Strike.

**Activate** Cast a Spell

**Effect** You expend a number of charges from the staff to cast a spell from its list. Add the cleric spells granted by your deity to the list for their rank and each higher rank. For example, a zealot staff of Sarenrae would add *breathe fire* at 1st through 7th rank, *fireball* at 3rd through 7th rank, and *wall of fire* at 4th through 7th rank.

- **Cantrip** [[Divine Lance]]
- **1st** [[Bane]]
- **2nd** [[Augury]]
- **3rd** [[Warding Aggression]]
- **4th** [[Divine Wrath]]
- **5th** [[Crisis of Faith]], [[Divine Wrath]]
- **6th** [[Spiritual Armament]], [[Zealous Conviction]]
- **7th** [[Crisis of Faith]], [[Divine Decree]]

**Craft Requirements** You worship the deity to which the staff is dedicated. Supply one casting of all listed spells, including your deity's cleric spells.

**Source:** `= this.source` (`= this.source-type`)
