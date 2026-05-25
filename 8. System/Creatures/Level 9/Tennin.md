---
type: creature
group: ["Angel", "Celestial"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Tennin"
level: "9"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Angel"
trait_02: "Celestial"
trait_03: "Holy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+17; [[Darkvision]]"
languages: "Diabolic, Draconic, Empyrean (Truespeech)"
skills:
  - name: Skills
    desc: "Acrobatics +19, Crafting +19, Performance +19, Religion +19, Society +17"
abilityMods: ["+2", "+6", "+3", "+2", "+4", "+6"]
abilities_top:
  - name: "Fingers Upon the Loom"
    desc: "The tennin can detect creatures wearing or holding any clothing as a precise sense with a range of 60 feet."
  - name: "Flawless Celestial Shawl"
    desc: "Each tennin has a unique *flawless celestial shawl*. A tennin without their *flawless celestial shawl* can't use their fly Speed or cast divine innate spells."
  - name: "Secrets of Immortality"
    desc: "The tennin can use Occultism instead of Medicine to `act administer-first-aid skill=occultism`, `act treat-disease skill=occultism`, `act treat-poison skill=occultism`, and [[Treat Wounds]]."
  - name: "Dancer Across the Heavens"
    desc: "The tennin can Step into difficult terrain and can use either their land or fly Speed to Step. Also, when the tennin attempts a Performance check to dance, they can Step or Stride as a free action."
armorclass:
  - name: AC
    desc: "27; **Fort** +16, **Ref** +21, **Will** +17"
health:
  - name: HP
    desc: "155; **Weaknesses** unholy 10; **Resistances** cold 10"
abilities_mid:
  - name: "Five Color Dance"
    desc: "30 feet. Any piece of clothing or equipment worn or held by an ally within the aura has its Hardness increased by 3, Hit Points increased by 20, and Broken Threshold increased by 10."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +20 (`pf2:1`) (agile, finesse, holy, magical, nonlethal), **Damage** 2d8+6 bludgeoning plus 2d6 spirit"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 29, attack +21<br>**5th** [[Truespeech]] (Constant), [[Wall of Ice]]<br>**4th** [[Unfettered Movement]] (Constant)<br>**3rd** [[Safe Passage]]<br>**2nd** [[Peaceful Rest]], [[Sure Footing]] (At Will)<br>**1st** [[Divine Lance]], [[Frostbite]], [[Heal]], [[Know the Way]], [[Sigil]]"
abilities_bot: []
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Celestial artisans and elegant dancers called tennins serve as Nirvana's attendants, where they weave the gods' marvelous, seamless garments from clouds and frost and entertain the courts with skyward dances, their footsteps lighter than dew. During catastrophic wars and disasters, tennins descend from Nirvana to mend what is broken and soothe those who suffer. The realm of Nirvana often promotes the virtuous souls of dutiful craftspeople and dedicated musicians to the ranks of the brocade angels so they might use their talents to bring beauty and kindness to a Universe overwhelmed by war.

It feels like there have always been too few tennins to attend to the needs of an entire world. Tragically, their numbers are dwindling in the wake of Gorum's death, which has sparked and renewed numerous conficts. Many angels have fallen or lost their way amid the discord.

```statblock
creature: "Tennin"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
