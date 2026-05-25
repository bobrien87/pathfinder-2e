---
type: creature
group: ["Azata", "Celestial"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Zhuraita"
level: "15"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Azata"
trait_02: "Celestial"
trait_03: "Holy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+28; [[Darkvision]], [[Truesight]] (precise) 60 feet"
languages: "Common, Diabolic, Draconic, Empyrean (Truespeech)"
skills:
  - name: Skills
    desc: "Acrobatics +25, Arcana +28, Athletics +25, Nature +28, Occultism +26, Religion +28"
abilityMods: ["+4", "+6", "+5", "+7", "+7", "+5"]
abilities_top: []
armorclass:
  - name: AC
    desc: "37; **Fort** +23, **Ref** +26, **Will** +29"
health:
  - name: HP
    desc: "280; **Weaknesses** cold iron 15, unholy 15"
abilities_mid:
  - name: "Deconstruct"
    desc: "`pf2:r` **Trigger** The zhuraita is targeted by an efect with the linguistic or mental trait <br>  <br> **Effect** The zhuraita critiques their enemy's theoretical underpinnings, attempting a counteract check with a bonus of `r 1d20+28#Counteract` (counteract rank 8). If the efect is counteracted, the triggering enemy becomes [[Frightened]] 1 ([[Frightened]] 2 if the zhuraita critically succeeded)."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Thesis +27 (`pf2:1`) (holy, magical), **Damage** 3d12+10 bludgeoning"
  - name: "Ranged strike"
    desc: "Looseleaf +27 (`pf2:1`) (holy, magical), **Damage** 3d10+10 slashing"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 36, attack +0<br>**6th** [[Truesight]] (Constant)<br>**5th** [[Truespeech]] (Constant)<br>**3rd** [[Hypercognition]]<br>**2nd** [[Clear Mind]], [[Translate]] (At Will)<br>**1st** [[Detect Magic]], [[Guidance]], [[Mindlink]] (At Will), [[Read Aura]]"
abilities_bot:
  - name: "Revealing Hypothesis"
    desc: "`pf2:0` **Requirements** The zhuraita hits a creature with its thesis <br>  <br> **Effect** The zhuraita's thesis opens, with the pages futtering at an unnatural speed. It then slams shut, with the cover now showing the image of the creature it hit. The zhuraita's Strikes against that creature deal an additional 2d6 precision damage. The zhuraita can only have one creature as the focus of its Revealing Hypothesis, which lasts until they target someone else."
  - name: "Thesis Shield"
    desc: "`pf2:1` A spinning circle of tomes surrounds the zhuraita, lasting until the start of their next turn. While Thesis Shield is active, the zhuraita gains a +2 circumstance bonus to AC and has the [[Concealed]] condition."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Zhuraitas are dedicated to the freedom of academic and scientifc inquiry, protecting the creativity and inventiveness of scholarly felds. Many good-hearted academics have breakthroughs due to a zhuraita's inspiration, notably with projects that have lasting positive impacts on others. Zhuraitas also travel to defend important centers of knowledge when they are in danger of destruction.

Zhuraitas despise those who would use research as a tool of oppression, and there are even rumors of them sabotaging such projects, hindering their completion. The azatas are known to sometimes hide away knowledge they believe to be harmful or dangerous. They don't outright destroy such knowledge, however, and instead choose to seal it away in places they can defend. On rare occasions, a zhuraita will recognize that such knowledge might actually be of some use for a trusted ally and share the information, though only under the zhuraita's supervision.

```statblock
creature: "Zhuraita"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
