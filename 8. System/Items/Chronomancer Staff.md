---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Magical]]", "[[Staff]]", "[[Two hand d8]]"]
price: "{'gp': 15000}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Clock faces and gears adorn the twisted iron shaft of a *chronomancer staff*, the hands of the clocks continually ticking or winding backward. Used as a weapon, the staff is a *+2 greater striking quickstrike staff*. While wielding this staff, you also gain a +1 circumstance bonus to initiative rolls.

**Activate** Cast a Spell

**Effect** You expend a number of charges from the staff to cast a spell from its list.

- **Cantrip** [[Time Sense]]
- **1st** [[Déjà Vu]], [[Synchronize]]
- **2nd** [[Loose Time's Arrow]], [[Synchronize]]
- **3rd** [[Day's Weight]], [[Haste]], [[Slow]], [[Time Jump]]
- **4th** [[Curse of Lost Time]]
- **5th** [[Quicken Time]], [[Rewinding Step]], [[Stagnate Time]]
- **6th** [[Cast into Time]], [[Day's Weight]]
- **7th** [[Time Beacon]]

**Craft Requirements** Supply one casting of all listed ranks of all listed spells.

**Source:** `= this.source` (`= this.source-type`)
