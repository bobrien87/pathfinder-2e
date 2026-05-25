---
type: creature
group: ["Fiend", "Sahkil"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Pakalchi"
level: "9"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Fiend"
trait_02: "Sahkil"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+18; [[Darkvision]], [[Truesight]] (precise) 60 feet"
languages: "Chthonian, Diabolic, Empyrean, Requian (Telepathy 100 feet, Truespeech)"
skills:
  - name: Skills
    desc: "Acrobatics +18, Deception +21, Diplomacy +21, Intimidation +21, Stealth +18"
abilityMods: ["+4", "+5", "+4", "+2", "+3", "+6"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Easy to Call"
    desc: "A pakalchi's level is considered 2 lower for the purpose of being conjured by the [[Binding Circle]] ritual (and potentially other rituals, at the GM's discretion), but it is always free to attack or leave instead of negotiate unless the primary caster's check is a critical success."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Betrayal Toxin"
    desc: "A creature affected by betrayal toxin hears whispers of incessant doubt in their head and can't treat any creature as their ally <br>  <br> **Saving Throw** DC 28 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** [[Stupefied 1]] (1 round) <br>  <br> **Stage 2** [[Stupefied 2]] (1 round)"
armorclass:
  - name: AC
    desc: "26; **Fort** +17, **Ref** +18, **Will** +20"
health:
  - name: HP
    desc: "150; **Immunities** fear effects, poison; **Weaknesses** holy 5"
abilities_mid:
  - name: "Entangling Train"
    desc: "`pf2:r` **Trigger** A creature moves adjacent to the pakalchi <br>  <br> **Effect** Writhing, pitch-black vines wrap around the creature. The creature takes 1d6 slashing damage and takes a -15-foot circumstance penalty to its Speeds until the end of its next turn. <br>  <br> > [!danger] Effect: Entangling Train"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Vine +18 (`pf2:1`) (finesse, reach 10 ft., unholy, versatile p), **Damage** 2d10+6 slashing plus 1d6 spirit plus 1d6 bleed plus [[Betrayal Toxin]]"
  - name: "Melee strike"
    desc: "Claw +18 (`pf2:1`) (agile, finesse, unarmed, unholy), **Damage** 2d10+6 slashing plus 1d6 spirit"
  - name: "Ranged strike"
    desc: "Thorn +18 (`pf2:1`) (agile, unholy, range 50 ft.), **Damage** 2d4+6 piercing plus 1d6 spirit plus 1d6 bleed plus [[Betrayal Toxin]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 30, attack +22<br>**7th** [[Mask of Terror (self only)]]<br>**6th** [[Dominate]], [[Truesight]] (Constant)<br>**5th** [[Truespeech]] (Constant)<br>**4th** [[Suggestion]] (At Will)<br>**2nd** [[Calm]]<br>**1st** [[Charm]], [[Detect Magic]]"
abilities_bot:
  - name: "Skip Between"
    desc: "`pf2:1` The sahkil moves from the Universe to the Ethereal Plane or vice-versa. While in the Ethereal Plane, they're unable to affect anything in the Universe, and they cannot be seen by beings or abilities in the Universe, unless these have an ability that can gaze into the Ethereal Plane. While on the Material Plane the inverse is true for anything on the Ethereal Plane. A summoned sahkil can't use Skip Between."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Pakalchis strive to intensify their preys' inherent insecurity over personal and emotional bonds, playing on the threat of those relationships falling into ruin. These sahkils are among the most manipulative of their kind, pulling strings both literal and figurative on their victims over stretched-out periods of time, exhilarating in the despair and fear for as long as possible.

Ages ago, when this cycle of the multiverse was still adolescent, a cabal of psychopomps who already felt bored and restrained in their role of ushering souls to their ultimate resting place rebelled against their station. It was this corruption of the cycle of souls that spawned the first sahkils.

Ambivalent to the prescribed order of the multiverse and spiteful of mortals, sahkils delight in spreading fear and unease to all beings, clogging up the metaphysical cycle with anxiety-ridden mortals too scared to achieve their potential. These fiends have drastically changed from their dedicated psychopomp predecessors. They are creatures of spite and torment, fear and disgust. They exploit the most common and rare fears for their own perverse satisfaction, and they want nothing more than to frighten mortals and make them quetion their reason for existence.

Most sahkils lurk on the Ethereal Plane, but they frequently invade the Material Plane to torment mortals and spread terror. They use their innate ability to slip between the veils of the Ethereal and Material effortlessly, often stalking their targets for days or weeks before enacting their devious plots.

```statblock
creature: "Pakalchi"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
