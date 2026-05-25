---
type: creature
group: ["Humanoid", "Titan"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Danava Titan"
level: "23"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Humanoid"
trait_02: "Titan"
trait_03: "Water"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+41; [[Darkvision]], [[Truesight]] (precise) 60 feet, [[Wavesense]] (imprecise) 100 feet"
languages: "Chthonian, Common, Empyrean, Thalassic (Telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +39, Arcana +43, Athletics +46, Crafting +43, Nature +41, Occultism +43, Religion +41, Society +43"
abilityMods: ["+11", "+8", "+10", "+10", "+8", "+6"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
armorclass:
  - name: AC
    desc: "49; **Fort** +41, **Ref** +37, **Will** +37"
health:
  - name: HP
    desc: "470; **Immunities** death effects, disease"
abilities_mid:
  - name: "+4 Status to All Saves vs. Mental or Divine"
    desc: ""
  - name: "Hadalic Presence"
    desc: "Creatures that fail their Will save against the titan's impossible stature aura also experience the crushing depths and darkness of the ocean floor. Such creatures see as if in an area of [[Darkness]] (10th rank), and the titan can use their wavesense to detect such creatures as a precise sense, even if neither are in water. On a critical failure, the creature is also [[Immobilized]]."
  - name: "Impossible Stature"
    desc: "100 feet. Titans warp perception and distance around them to seem even larger and more imposing. A creature that enters or begins its turn within the emanation must succeed at a DC 46 [[Will]] save or its movement toward the titan is movement over difficult terrain (greater difficult terrain on a critical failure) for 1 round."
  - name: "Relentless"
    desc: "The titan is as ever-moving as ocean waves. They're permanently [[Quickened]], and the extra action can be used only to Stride, Strike, or Sustain a Spell, or as one of the actions necessary to cast [[Dispel Magic]]."
  - name: "Roiling Rebuke"
    desc: "`pf2:r` **Trigger** A creature within 200 feet targets the titan with or includes the titan in the area of an attack, spell, or other effect <br>  <br> **Effect** The titan makes a benthic wave Strike against the triggering creature. If the Strike hits, the titan disrupts the triggering action."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Greatclub +43 (`pf2:1`) (backswing, magical, reach 40 ft., shove), **Damage** 2d12 cold plus 4d10+20 bludgeoning"
  - name: "Melee strike"
    desc: "Foot +40 (`pf2:1`) (agile, reach 30 ft.), **Damage** 2d12 cold plus 4d8+20 bludgeoning"
  - name: "Ranged strike"
    desc: "Benthic Wave +40 (`pf2:1`) (brutal, magical, water), **Damage** 2d12 cold plus 4d6+20 bludgeoning"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 46, attack +38<br>**9th** [[Implosion]]<br>**7th** [[Eclipse Burst]]<br>**6th** [[Truesight]] (Constant)<br>**5th** [[Control Water]] (At Will)<br>**4th** [[Hydraulic Torrent]]<br>**2nd** [[Dispel Magic]] (At Will), [[Water Walk]] (Constant)<br>**1st** [[Heal]], [[Hydraulic Push]]"
abilities_bot:
  - name: "Trample"
    desc: "`pf2:3` Huge or smaller, foot, DC 46 [[Reflex]] save <br>  <br> The monster Strides up to double its Speed and can move through the spaces of creatures of the listed size, Trampling each creature whose space it enters. The monster can attempt to Trample the same creature only once in a single use of Trample. The monster deals the damage of the listed Strike, but trampled creatures can attempt a basic Reflex save at the listed DC (no damage on a critical success, half damage on a success, double damage on a critical failure)."
  - name: "Wide Cleave"
    desc: "`pf2:2` The titan makes a melee weapon Strike against each foe within their reach. This counts as three attacks for the titan's multiple attack penalty, but the penalty doesn't increase until all attacks have been made."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Danava titans once regulated the foundational forces that shaped reality. Rebuked by the gods for being harsh and inflexible overseers, these spurned titans joined their siblings in the failed war against their creators. Defeated, the danavas were cast into the paralyzing depths of the cosmos's seas. The few danava titans who have escaped now wield the cold, darkness, and crushing pressure of their prisons in pursuit of their ancient visions of reality. Danavas split mountains, wake primordial beasts, or level whole civilizations in accordance with grand designs they forged at the dawn of time. Others hunt and harvest the balance-enforcing aeons, whom they see as usurpers of their divine responsibility.

Created by ancient deities long before the rise of mortal ancestries, titans united and attempted to overthrow their deific progenitors. The resulting war still figures prominently throughout mortal myths, in which most titans were cast down and imprisoned for eons.

```statblock
creature: "Danava Titan"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
