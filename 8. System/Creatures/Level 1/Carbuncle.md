---
type: creature
group: ["Beast"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Carbuncle"
level: "1"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Tiny"
trait_01: "Beast"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+7; [[Darkvision]]"
languages: "carbuncle empathy 30 feet"
skills:
  - name: Skills
    desc: "Stealth +3, Survival +6"
abilityMods: ["-3", "+0", "+3", "-2", "+3", "+0"]
abilities_top:
  - name: "Carbuncle Empathy"
    desc: "The carbuncle can [[Telepathically]] send mild feelings and sensations to nearby creatures. It can't use this ability to communicate in language or hinder a target, but it might convey a feeling of dread or the scent of food cooking nearby."
  - name: "Treasure Sense"
    desc: "The carbuncle can sense the presence and location of any object or grouping of objects worth at least 50 gp in total within 500 feet of it. The carbuncle's sense only functions if the treasure is within in a container or physically obscured, such as when buried underground. Objects worn on a person or left out in open air don't trigger the carbuncle's sense."
armorclass:
  - name: AC
    desc: "16; **Fort** +8, **Ref** +3, **Will** +6"
health:
  - name: HP
    desc: "20"
abilities_mid:
  - name: "Easy to Influence"
    desc: "Any mental spell can affect a carbuncle, regardless of creature type limitations. Against a [[Suggestion]] spell, a carbuncle always gets an outcome one degree of success worse than it rolled on its saving throw."
  - name: "Fatal Faker"
    desc: "`pf2:r` **Trigger** The carbuncle takes damage <br>  <br> **Effect** The carbuncle feigns death by teleporting away and leaving a replica of its corpse behind, creating a colorful flash of light and a croaking sound. The real carbuncle transports to a clear space within 30 feet that it can see, and a hollow shell remains behind. The fake body appears solid until it is touched, at which point it crumbles to dust."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +5 (`pf2:1`) (finesse, unarmed), **Damage** 1d6 piercing"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 18, attack +8<br>**3rd** [[Levitate (at will, self only)]]<br>**1st** [[Daze]], [[Jump]] (At Will)"
abilities_bot:
  - name: "Specious Suggestion"
    desc: "`pf2:2` **Frequency** three times per day <br>  <br> **Effect** The carbuncle concentrates on a creature it can see and tries to manipulate that creature, imploring them to perform harmless, pointless, and usually embarrassing actions. The target must attempt a DC 18 [[Will]] save. The target then becomes temporarily immune for 24 hours. This has the ef ects of [[Suggestion]] except that a critical success bolsters the target and grants them a +1 status bonus to Will saves for 1 hour, the duration on a failure is 1 round, and the duration on a critical failure is a 1 minute. The target can attempt a new save at the end of its turn each round to end the ef ect."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Never have legend and misinformation met upon a more inauspicious brow than that of the lowly carbuncle. At frst glance, they appear to be little more than ungainly reptiles. What sets them apart are their strange magical abilities and the gemstone-like horn protruding from between their goggling eyes. Although rumors suggest various uses for carbuncle horns, ranging from miracle cure-alls to potent magical components, the truth is much more mundane: a carbuncle's horn is merely a highly refective growth, not unlike a fngernail.

Carbuncles also possess a strange sense that allows them to detect treasure that has been hidden or obscured. The creatures generally feel a compulsion to move toward these treasures and remain nearby. Strangely, carbuncles seem disinterested once the valuables are laid out in the open, as if the obfuscation were part of their interest. Many would-be treasure hunters end up following the creatures in hopes of fnding treasures, though the fearfulness of carbuncles makes this a very diffcult prospect. Most carbuncles abandon their nests after being scared away, even when their sense would typically draw them back.

```statblock
creature: "Carbuncle"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
