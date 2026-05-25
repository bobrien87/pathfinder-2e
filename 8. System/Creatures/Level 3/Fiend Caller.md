---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Fiend Caller"
level: "3"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+8"
languages: "Chthonian, Common, Daemonic, Diabolic, Requian"
skills:
  - name: Skills
    desc: "Deception +10, Diplomacy +15, Intimidation +10, Occultism +16, Religion +13, Society +12, Fiend Lore +18, Legal Lore +18"
abilityMods: ["+2", "+2", "+0", "+4", "+1", "+3"]
abilities_top:
  - name: "Legal Specialist"
    desc: "For encounters involving contracts and negotiations, the fiend caller is an 8th-level challenge."
  - name: "Fiendish Contract"
    desc: "The fiend caller spends 1 day of downtime setting up a bargain between a mortal creature and a fiend the fiend caller knows well. The fiend caller attempts a Legal Lore check against the higher of the fiend's Legal lore check{Will DC} or Legal lore check{Diplomacy DC}. <br> - **Success** The mortal party receives one favor from the fiend, or the fiend becomes the mortal's minion for 1d4 days if they're on the same plane. Alternatively, if the GM allows the option, the mortal can receive a bargained contract of the fiend's level or lower. <br> - **Failure** The fiend caller fails to strike the bargain. <br> - **Critical Failure** The process fails, and the magical backlash makes the fiend caller [[Drained]] 2."
  - name: "Fiendish Ritualist"
    desc: "A fiend caller can cast [[Binding Circle]] and [[Commune]] to contact fiends even though the rituals are beyond the normal rank the fiend caller could cast. Furthermore, they can use Legal Lore for the primary check when they do so instead of the listed skill."
  - name: "Planar Communique"
    desc: "A fiend caller can cast [[Sending]] at will as an occult innate spell, but only to target a fiend they know well. The fiend can be on any plane."
armorclass:
  - name: AC
    desc: "17; **Fort** +7, **Ref** +9, **Will** +8"
health:
  - name: HP
    desc: "35"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +9 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4+6 piercing plus 1d4 bleed"
  - name: "Melee strike"
    desc: "Dagger +9 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 1d4 bleed plus 1d4+6 piercing"
  - name: "Melee strike"
    desc: "Fist +9 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+6 bludgeoning"
spellcasting:
  - name: "Occult Prepared Spells"
    desc: "DC 20, attack +12<br>**2nd** (3 slots) [[Calm]], [[Paranoia]], [[Spiritual Armament]]<br>**1st** (4 slots) [[Command]], [[Fear]], [[Force Barrage]], [[Grim Tendrils]]<br>**Cantrips** [[Detect Magic]], [[Message]], [[Sigil]], [[Telekinetic Hand]], [[Void Warp]]"
  - name: "Occult Innate Spells"
    desc: "DC 20, attack +12<br>**5th** [[Sending (At-Will)]]"
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Fiend callers act as intermediaries to help mortals sell their souls or make other deals with fiends. You can adjust a fiend caller to be accompanied by a bound fiend. The fiend gains the minion trait, and you can replace the fiend caller's [[Spiritual Armament]] spell with [[Final Sacrifice]].

Villains pursue selfish and cruel goals, trampling over anyone in their way.

```statblock
creature: "Fiend Caller"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
