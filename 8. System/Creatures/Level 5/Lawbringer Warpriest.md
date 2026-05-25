---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Lawbringer Warpriest"
level: "5"
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
    desc: "+11; [[Darkvision]]"
languages: "Common, Empyrean"
skills:
  - name: Skills
    desc: "Athletics +11, Diplomacy +11, Medicine +10, Religion +12, Society +7"
abilityMods: ["+4", "+1", "+3", "+0", "+3", "+2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "23; **Fort** +12, **Ref** +8, **Will** +12"
health:
  - name: HP
    desc: "64"
abilities_mid:
  - name: "Responsive Recovery"
    desc: "`pf2:r` **Trigger** One of the lawbringer's allies is reduced to 0 Hit Points <br>  <br> **Requirements** The lawbringer has a *heal* spell prepared <br>  <br> **Effect** Before the ally falls [[Unconscious]] or dies, the lawbringer Strides toward them and casts a 2-action [[Heal]] spell targeting the ally. The ally remains standing."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Greatsword +13 (`pf2:1`) (versatile p), **Damage** 1d12+7 slashing"
  - name: "Ranged strike"
    desc: "Crossbow +11 (`pf2:1`) (reload 1, range 120 ft.), **Damage** 1d8+3 piercing"
spellcasting:
  - name: "Divine Prepared Spells"
    desc: "DC 20, attack +12<br>**3rd** (2 slots) [[Blindness]], [[Haste]]<br>**2nd** (3 slots) [[Enlarge]], [[Harm]], [[Heal]]<br>**1st** (3 slots) [[Harm]], [[Heal]], [[Sure Strike]]<br>**Cantrips** [[Daze]], [[Divine Lance]], [[Forbidding Ward]], [[Guidance]], [[Light]]"
  - name: "Domain Spells"
    desc: "DC 20, attack +12<br>**1st** [[Athletic Rush]]"
abilities_bot:
  - name: "Channel Smite"
    desc: "`pf2:2` **Requirements** The lawbringer has a [[Heal]] or [[Harm]] spell prepared <br>  <br> **Effect** The lawbringer makes a melee Strike and expends a *harm* or *heal* spell. On a hit, they cast the 1-action version of the spell to damage the target. The target automatically gets a failure on its save (or a critical failure if the lawbringer's Strike was a critical hit). The spell doesn't have the manipulate trait when cast this way."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Mortals whose ancestry has been influenced by archons are called lawbringers. They may have mortal ancestors who fought alongside archons against the forces of evil and entropy, or they may have been born from a union between an archon and a mortal. Many lawbringers seek adventure to bringing order to the world.

Many immortals dwell upon the other planes of the Great Beyond. Some are benevolent and kind, like angels. Others are cruel and destructive, like demons. And some fit roles outside of morality, like psychopomps. It's far from unheard of for mortals and immortals alike to become entangled romantically, and the children of such engagements carry a supernatural element in their bloodlines for generations to follow. After the first generation, this otherworldly influence usually lies dormant, but now and then, the influence can manifest strongly in descendants many years later. These inheritors of extraplanar legacies are known collectively as planar scions.

Nephilim
Nephilim are planar scions with a connection to the planes of the Outer Sphere. Some are obviously tied to realms such as Heaven or Hell, while others are cryptic amalgams of metaphysical traits.

```statblock
creature: "Lawbringer Warpriest"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
