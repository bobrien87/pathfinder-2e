---
type: creature
group: ["Beast"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Sphinx"
level: "8"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Beast"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+18; [[Darkvision]]"
languages: "Common, Draconic, Sphinx (Truespeech)"
skills:
  - name: Skills
    desc: "Arcana +17, Athletics +18, Deception +16, Diplomacy +16, Intimidation +18, Occultism +17, Bardic Lore +19"
abilityMods: ["+6", "+1", "+3", "+5", "+4", "+4"]
abilities_top:
  - name: "Bardic Lore"
    desc: "Sphinxes are naturally curious, and their love of puzzles and mysteries leads them to gather information on a broad range of topics. Sphinxes have Bardic Lore, a special Lore skill that can be used only to Recall Knowledge, but on any topic."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Riddler's Rune"
    desc: "Once per week, a Sphinx can create a magical symbol as the [[Rune Trap]] ritual. The sphinx usually shapes it to take the form of a written riddle and sets the password to the answer. <br>  <br> A creature that gives the wrong answer or tries to pass without answering must succeed at a DC 26 [[Will]] save or be affected by one of the following spells, chosen by the sphinx when creating the symbol: [[Synaptic Pulse]] (5th), [[Charm]] (4th), [[Fear]] (4th), [[Phantom Pain]] (4th), [[Sleep]] (4th). The sphinx learns the identity of any creature that answers the riddle and tends to be friendly to them if they answered correctly."
armorclass:
  - name: AC
    desc: "27; **Fort** +16, **Ref** +14, **Will** +19"
health:
  - name: HP
    desc: "135"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +20 (`pf2:1`) (agile, unarmed), **Damage** 2d6+9 slashing"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 27, attack +19<br>**5th** [[Truespeech]] (Constant)<br>**4th** [[Clairvoyance]] (At Will), [[Read Omens]]<br>**3rd** [[Clairaudience]] (At Will), [[Locate]]<br>**2nd** [[Cleanse Affliction]], [[Dispel Magic]], [[See the Unseen]] (Constant)<br>**1st** [[Detect Magic]]"
abilities_bot:
  - name: "Claw Rake"
    desc: "`pf2:3` The sphinx rears back on their hind legs and makes two claw Strikes at the same target, using the same attack bonus as their highest melee attack. If both attacks deal damage, the target takes extra damage equal to one claw Strike."
  - name: "Pounce"
    desc: "`pf2:1` The sphinx Strides and makes a Strike at the end of that movement. If the sphinx began this action [[Hidden]], they remain hidden until after the attack."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Sphinxes are mystical beings with the body of a lion, the wings of a great bird, and the upper torso and head of a human. They are often maligned in legends as nothing more than monsters, and though they are quick to anger and are capable of exacting deadly retribution for perceived slights, they are also very intelligent.

Sphinxes are often associated with desert regions, but they can dwell in more moderate climates as well. They form small groups consisting of a single, extended family that hunts and works together to protect and teach their young. As they mature, sphinxes develop a wanderlust, a drive to gather hidden lore and solve the world's greatest riddles-the trait that is perhaps most often identified with their kind.

While sometimes bound into service as guardians for powerful spellcasters, lone sphinxes may also be encountered on journeys of discovery and as purveyors of esoteric lore. If treated with the proper respect-and fed well-a sphinx can demonstrate a willingness to exchange information. Their favorite currency is, of course, riddles and secrets. One who can trade knowledge for knowledge has a much better chance of succeeding while bargaining with a sphinx. However, a sphinx's insatiable thirst for new riddles as well their extensive collection of secrets accumulated over hundreds of years of life-makes it difficult to offer them something they don't already know. Those who attempt to trade petty insight and stale riddles may invoke a sphinx's ire and will not live long enough to regret it.

```statblock
creature: "Sphinx"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
