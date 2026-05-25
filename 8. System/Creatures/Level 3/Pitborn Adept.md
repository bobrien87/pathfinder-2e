---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Pitborn Adept"
level: "3"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Nephilim"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+6; [[Darkvision]]"
languages: "Chthonian, Common"
skills:
  - name: Skills
    desc: "Acrobatics +7, Arcana +9, Deception +9, Intimidation +7, Occultism +9, Religion +6, Society +9, Stealth +7, Outer Rifts Lore +9"
abilityMods: ["+0", "+2", "+0", "+4", "+1", "+2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "17; **Fort** +5, **Ref** +7, **Will** +8"
health:
  - name: HP
    desc: "29"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Staff +6 (`pf2:1`) (two hand d8), **Damage** 1d6 bludgeoning"
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 21, attack +11<br>**2nd** (2 slots) [[Floating Flame]], [[Invisibility]]<br>**1st** (3 slots) [[Charm]], [[Enfeeble]], [[Force Barrage]]<br>**Cantrips** [[Detect Magic]], [[Shield]], [[Tangle Vine]], [[Telekinetic Hand]], [[Void Warp]]"
  - name: "Divine Innate Spells"
    desc: "DC 17, attack +9<br>**2nd** [[Darkness]]"
abilities_bot:
  - name: "Drain Bonded Item"
    desc: "`pf2:0` **Frequency** once per day <br>  <br> **Requirements** The adept hasn't acted yet on this turn <br>  <br> **Effect** The adept expends the power stored in its staff. This gives the adept the ability to cast one prepared spell it had already previously cast today (choosing a different spell rank each time), without spending a spell slot. The adept must still Cast the Spell and meet the spell's other requirements."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

One of the most common types of nephilim is the pitborn, who bear a demonic corruption infesting their mortal bloodline.

Many immortals dwell upon the other planes of the Great Beyond. Some are benevolent and kind, like angels. Others are cruel and destructive, like demons. And some fit roles outside of morality, like psychopomps. It's far from unheard of for mortals and immortals alike to become entangled romantically, and the children of such engagements carry a supernatural element in their bloodlines for generations to follow. After the first generation, this otherworldly influence usually lies dormant, but now and then, the influence can manifest strongly in descendants many years later. These inheritors of extraplanar legacies are known collectively as planar scions.

Nephilim
Nephilim are planar scions with a connection to the planes of the Outer Sphere. Some are obviously tied to realms such as Heaven or Hell, while others are cryptic amalgams of metaphysical traits.

```statblock
creature: "Pitborn Adept"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
