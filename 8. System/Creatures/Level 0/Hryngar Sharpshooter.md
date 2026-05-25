---
type: creature
group: ["Duergar", "Dwarf"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Hryngar Sharpshooter"
level: "0"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Duergar"
trait_02: "Dwarf"
trait_03: "Humanoid"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+4; [[Darkvision]]"
languages: "Common, Dwarven, Sakvroth"
skills:
  - name: Skills
    desc: "Athletics +3, Stealth +5"
abilityMods: ["+1", "+3", "+3", "+0", "+2", "-2"]
abilities_top:
  - name: "Bola Bolt"
    desc: "This shot deals no damage, but on a hit, the target must succeed at a DC 16 [[Reflex]] save or be knocked [[Prone]] and [[Immobilized]] until it is freed with a successful DC 15 check to `act escape dc=15`. This check can be attempted either by the target or a creature adjacent to the target."
armorclass:
  - name: AC
    desc: "15; **Fort** +7, **Ref** +7, **Will** +4"
health:
  - name: HP
    desc: "18"
abilities_mid:
  - name: "+2 Status to All Saves vs. Magic"
    desc: ""
  - name: "Light Blindness"
    desc: "When first exposed to bright light, the monster is [[Blinded]] until the end of its next turn. After this exposure, light doesn't blind the monster again until after it spends 1 hour in darkness. However, as long as the monster is in an area of bright light, it's [[Dazzled]]."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Light Mace +5 (`pf2:1`) (agile, finesse, shove), **Damage** 1d4+1 bludgeoning"
  - name: "Ranged strike"
    desc: "Crossbow +7 (`pf2:1`) (reload 1, range 120 ft.), **Damage** 1d8 piercing plus [[Bolts]]"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 12, attack +4<br>**2nd** [[Blood Vendetta]], [[Paranoia]]<br>**1st** [[Sigil]]"
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Hryngar sharpshooters serve both as ranged support for caravans and as snipers posted on guard towers overlooking quarries and other areas where workers toil away the hours. Hryngar sharpshooters also specialize in nonlethal methods of ranged combat—tactics they are often called upon to use when tracking down derelict debtors or those attempting to flee from their contractual obligations.

Deep beneath the surface, the dour dwarves known as hryngars stubbornly toil, claiming the ancestral subterranean homelands of other dwarves as their own. Long ago, hryngar leaders refused to venture to the surface along with their "cousins," forsaking the Quest for Sky. An exiled dwarven deity named Droskar offered hryngars salvation from the horrors that beset them in the Darklands, offering them power, cunning, and knowledge in exchange for their unending servitude. Many hryngar believe that by working harder than their brethren, they can build a society far greater than anything under the sun, claiming unending riches from the planet's metallic veins in days of relentless toil.

Through Droskar's blessings and their own fearsome work ethic, hryngar kingdoms now rule a significant portion of the upper Darklands region of NarVoth, and it's common to see hryngar caravans moving through the tunnels, drawn by teams of immense beetles. Hryngar leadership typically consists of powerful divine servants of Droskar, along with fearsomely implacable warriors whose martial prowess, backed by innate occult magic, ensures they can overcome any direct threat to hryngar rule. Almost every aspect of hryngar society is controlled by a strict hierarchy of leadership, with taskmasters directing subordinates across all walks of life.

```statblock
creature: "Hryngar Sharpshooter"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
