---
type: creature
group: ["Air", "Beast"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Harpy"
level: "5"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Air"
trait_02: "Beast"
trait_03: "Humanoid"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+12; [[Darkvision]]"
languages: "Common (Wind's Whispers)"
skills:
  - name: Skills
    desc: "Acrobatics +13, Deception +11, Intimidation +13, Performance +11, Stealth +11, Thievery +13"
abilityMods: ["+1", "+4", "+0", "-1", "+1", "+2"]
abilities_top:
  - name: "Wind's Whispers"
    desc: "When a harpy speaks, they can choose one creature within 90 feet. That creature can hear the harpy's words over any other sound, but no other creature hears the words at all."
  - name: "Putrid Plague"
    desc: "The sickened and unconscious conditions from putrid plague can't end or be reduced until the disease is cured <br>  <br> **Saving Throw** DC 19 [[Fortitude]] save <br>  <br> **Stage 1** carrier with no ill effect (1d4 hours), <br>  <br> **Stage 2** [[Sickened]] 1 (1 day), <br>  <br> **Stage 3** sickened 1 and [[Slowed]] 1 (1 day), <br>  <br> **Stage 4** [[Unconscious]] (1 day), <br>  <br> **Stage 5** dead"
armorclass:
  - name: AC
    desc: "21; **Fort** +9, **Ref** +15, **Will** +12"
health:
  - name: HP
    desc: "75"
abilities_mid:
  - name: "Stench"
    desc: "30 feet. DC 21 [[Fortitude]] save <br>  <br> A creature entering the aura or starting its turn in the area must succeed at a Fortitude save or become [[Sickened]] 1 (plus [[Slowed]] 1 as long as it's sickened on a critical failure). A creature that succeeds at its save or recovers from being sickened is temporarily immune to all stench auras for 1 minute."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Talon +15 (`pf2:1`) (agile, finesse, unarmed), **Damage** 2d6+4 slashing"
  - name: "Melee strike"
    desc: "Jaws +15 (`pf2:1`) (finesse, unarmed), **Damage** 2d8+4 piercing plus [[Putrid Plague]]"
spellcasting: []
abilities_bot:
  - name: "Hungry Winds"
    desc: "`pf2:2` The harpy uses the wind to pull its prey closer. A target within 20 feet must succeed at a DC 21 [[Fortitude]] save or be pulled adjacent to the harpy, where they make a jaws Strike against the target. If the target was pulled off the ground and can't fly, it then falls as normal."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Harpies are amalgamations of human and bird, resembling feral humans with wings, talons, and sharp teeth. They use their ancestral control of the wind to lure prey or even directly pull in their next meal. They enjoy causing confusion and fear in their prey before they strike, believing it creates a savory flavor in the flesh. Harpies can eat most creatures but strongly prefer sapient prey—humans and elves in particular. Although harpies will eat goblins if sufficiently hungry, they dislike their flavor and avoid eating them if possible. This doesn't comfort goblins, of course, who have a particularly strong fear of harpies.

Because their aeries often reek with the gore of their kills and careless spatters of guano, harpies carry a distinctly vile scent that canny travelers associate with danger. Harpies who roost close to civilization make better efforts to keep clean, though these efforts have mixed results.

Somewhere among the filth, most aeries have a shrine dedicated to the demon lord Pazuzu. Harpy legends credit him with raising them up from simple air spirits to their current station, and their gratitude typically takes the shape of a sketched figure in a corner piled with offerings. More devout families build portable wooden shrines that are carried from aerie to aerie for generations.

Harpies live in family groups or larger clans. Most adults stand 5 feet tall and weigh around 90 pounds. While some use relatively simple weapons, those who master the use of the bow are regarded as heroes among their kind.

```statblock
creature: "Harpy"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
