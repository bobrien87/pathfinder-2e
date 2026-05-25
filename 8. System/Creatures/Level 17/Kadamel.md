---
type: creature
group: ["Archon", "Celestial"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Kadamel"
level: "17"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Archon"
trait_02: "Celestial"
trait_03: "Holy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+34; [[Darkvision]], [[Truesight]] (precise) 60 feet"
languages: "Diabolic, Draconic, Empyrean, Utopian (Truespeech)"
skills:
  - name: Skills
    desc: "Athletics +32, Diplomacy +30, Intimidation +32, Religion +34"
abilityMods: ["+9", "+5", "+7", "+4", "+9", "+7"]
abilities_top:
  - name: "Stone Shield"
    desc: "The kadamel can create a stone shield for defense, which grants a +2 circumstance bonus to AC and has Hardness 15, HP 120, and BT 60."
armorclass:
  - name: AC
    desc: "40 all-around vision; **Fort** +29, **Ref** +26, **Will** +32"
health:
  - name: HP
    desc: "300; **Immunities** fear effects; **Weaknesses** unholy 15"
abilities_mid:
  - name: "All-Around Vision"
    desc: "This monster can see in all directions simultaneously and therefore can't be flanked."
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Archon's Protection"
    desc: "`pf2:r` **Trigger** An enemy damages the archon's ally and both are within 15 feet of the archon <br>  <br> **Effect** The ally gains resistance 20 to all damage against the triggering damage, and the archon can make a Strike against the enemy. <br>  <br> > [!danger] Effect: Archon's Protection"
  - name: "Patience of Stone"
    desc: "10 feet. Any enemy that ends its turn in the aura must succeed at a DC 36 [[Fortitude]] save or be [[Slowed]] 1 for 1 minute. If the creature succeeds, it's temporarily immune for 24 hours."
  - name: "Shield Block"
    desc: "`pf2:r` **Trigger** The monster has its shield raised and takes damage from a physical attack. <br>  <br> **Effect** The monster snaps its shield into place to deflect a blow. The shield prevents the monster from taking an amount of damage up to the shield's Hardness. The monster and the shield each take any remaining damage, possibly breaking or destroying the shield."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Stone Axe +32 (`pf2:1`) (holy, magical, sweep), **Damage** 3d10+15 slashing plus 2d12 electricity"
  - name: "Melee strike"
    desc: "Stone Axe +32 (`pf2:1`) (brutal, holy, magical, thrown 20), **Damage** 3d10+15 slashing plus 2d12 electricity"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 38, attack +30<br>**7th** [[Interplanar Teleport]], [[Planar Seal]]<br>**6th** [[Blessed Boundary]], [[Truesight]] (Constant)<br>**5th** [[Truespeech]] (Constant)<br>**4th** [[Planar Tether]], [[Translocate]] (At Will)<br>**3rd** [[Veil of Privacy]] (Constant)<br>**1st** [[Light]]"
abilities_bot:
  - name: "Calcifying Cloud"
    desc: "`pf2:2` **Requirements** The kadamel hit with a stone axe Strike during its most recent action <br>  <br> **Effect** The kadamel's axe explodes into calcifying powder. The creature the axe hit and each non-archon creature in a @Template[type:emanation|distance:5] must succeed at a DC 38 [[Fortitude]] save or become [[Slowed]] 1 for 1 minute. If the creature was already slowed by one of the kadamel's abilities, a failed save causes it to be [[Petrified]] permanently."
  - name: "Guardian Glyph"
    desc: "`pf2:1` **Frequency** once per day <br>  <br> **Effect** The kadamel alters the inscriptions on their body to store an 8th-rank spell, choosing from [[Divine Decree]], [[Divine Immolation]], [[Divine Wrath]], or [[Planar Seal]]. While storing the spell, the kadamel chooses an area they're guarding, typically a room containing a planar portal. When an intruder enters the area, the spell is cast automatically and expended. If the spell is targeted, it targets the triggering creature, and if it has an area, the area is centered on the triggering creature. Noticing the glyph requires a successful DC 38 [[Perception]] check. The glyph has an unlimited duration and ends if the kadamel uses this ability again or Dismisses the glyph."
  - name: "Re-Arm"
    desc: "`pf2:0` The kadamel forms a new stone axe or stone shield in a free hand"
  - name: "Statue"
    desc: "`pf2:1` Until the next time they act, the kadamel appears to be a statue. They have an automatic result of 50 on Deception checks and DCs to pass as a statue. While remaining motionless in this way, the kadamel has fast healing 20."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Fiends spread corruption to places across the planes—every place they can reach. Kadamels guard the most crucial pathways and holy sanctums. They hold a patient vigil, never distracted from their task. Most crucially, they watch over planar portals, barring passage to all but the most powerful fends. When encountered, these archons speak and react little. They rarely even move or react, though they readily accept any assistance in defeating fendish invaders. Even this, they accept with only an ominous nod.

```statblock
creature: "Kadamel"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
