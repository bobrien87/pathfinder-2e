---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Magical]]", "[[Staff]]", "[[Two hand d8]]"]
price: "{'gp': 1400}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A *spellstriker staff* is wrought iron with gleaming arcane sigils etched into its surface and a sharp point at the bottom. Used as a weapon, the staff is a *+2 striking shifting staff*.

**Activate** `pf2:f` (concentrate)

**Frequency** once per hour

**Trigger** You use Spellstrike with a non-cantrip spell and miss with the Strike

**Effect** An explosion of magical energy—stored up for the Spellstrike—explodes out. All creatures in a @Template[emanation|distance:5] take 1d6 damage per rank of the spell, with a [[Reflex]] save against your spell DC. This damage is the same type the spell would have dealt, and the activation gains that trait; if the spell would have dealt multiple types of damage, choose one of them. If the damage of the explosion is mental, the save is [[Will]] save instead of Reflex.

**Activate** Cast a Spell

**Effect** You expend a number of charges from the staff to cast a spell from its list.

- **Cantrip** [[Ignition]]
- **1st** [[Echoing Weapon]], [[Sure Strike]]
- **2nd** [[Acid Grip]], [[Telekinetic Maneuver]]
- **3rd** [[Echoing Weapon]], [[Haste]]
- **4th** [[Acid Grip]], [[Weapon Storm]]

**Craft Requirements** You have the magus's [[Spellstrike]] activity. Supply one casting of all listed ranks of all listed spells.

**Source:** `= this.source` (`= this.source-type`)
