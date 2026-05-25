---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Tree Singer"
level: "13"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+22"
languages: "Common, Wildsong"
skills:
  - name: Skills
    desc: "Athletics +23, Diplomacy +25, Intimidation +23, Nature +26, Performance +27, Survival +22"
abilityMods: ["+4", "+3", "+1", "+2", "+3", "+4"]
abilities_top:
  - name: "Plant Empathy"
    desc: "The tree singer can ask questions of, receive answers from, and use the Diplomacy skill with plants and fungus."
armorclass:
  - name: AC
    desc: "32; **Fort** +23, **Ref** +21, **Will** +25"
health:
  - name: HP
    desc: "220"
abilities_mid:
  - name: "Bloodthirsty Plants"
    desc: "`pf2:r` **Trigger** An enemy in the tree singer's Verdant Aria aura (see below) attacks one of the tree singer's allies <br>  <br> **Effect** Vines and branches to lash out at the attacker, dealing 3d6 piercing damage."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Longspear +24 (`pf2:1`) (magical, reach 10 ft.), **Damage** 2d8+10 piercing plus 2d10 sonic"
  - name: "Melee strike"
    desc: "Fist +23 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+10 bludgeoning plus 2d10 sonic"
  - name: "Ranged strike"
    desc: "Composite Longbow +23 (`pf2:1`) (deadly d10, magical, propulsive, reload 0, volley 30, range 100 ft.), **Damage** 2d8+8 piercing plus 1d10 sonic"
spellcasting:
  - name: "Primal Prepared Spells"
    desc: "DC 33, attack +25<br>**7th** (2 slots) [[Regenerate]], [[Tree of Seasons]]<br>**6th** (3 slots) [[Plant Form]], [[Tangling Creepers]], [[Wall of Thorns]]<br>**5th** (3 slots) [[Elemental Form (Wood Only)]], [[Nature's Pathway]], [[Plant Form]]<br>**4th** (3 slots) [[Oaken Resilience]], [[Resist Energy]], [[Vapor Form]]<br>**3rd** (3 slots) [[Earthbind]], [[Earthbind]], [[Slow]]<br>**2nd** (3 slots) [[Entangling Flora]], [[One with Plants]], [[One with Plants]]<br>**1st** (3 slots) [[Gentle Landing]], [[Gentle Landing]], [[Ventriloquism]]<br>**Cantrips** [[Detect Magic]], [[Light]], [[Prestidigitation]], [[Stabilize]], [[Tangle Vine]]"
  - name: "Druid Order Spells"
    desc: "DC 33, attack +25<br>**1st** [[Cornucopia]]"
abilities_bot:
  - name: "Verdant Aria"
    desc: "`pf2:1` The tree singer raises their voice in a haunting melody, creating an aura in a 30-foot emanation. Plants in the aura seem to come to life, swaying and rustling in response to the music. The tree singer's allies in the aura gain a +2 status bonus to AC and saving throws as the foliage around them shields and defends them from harm. <br>  <br> The aura lasts until the end of the tree singer's next turn but can be Sustained. It can be Sustained even if the tree singer is polymorphed. The effect ends early if the tree singer stops singing."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Singers can speak the words of creation in song, a forgotten art from the First World. Their melodies turn grass into blades and make trees stir. Through their music, plants rise to defend and seek vengeance for nature. Taught by woodland spirits or fey agents of the First World, they master the magic of primal song.

A primalist is a wielder of primal energies and magic, sometimes taught by forces of primal power, including powerful elementals or fey of the First World. Primalists protect the natural world, offering strong medicine to those in need while facing suspicion from those who don't understand their ways.

A great many primalists belong to druidic circles, and even those who aren't members tend to be familiar with the most prominent ones in their homeland.

```statblock
creature: "Tree Singer"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
