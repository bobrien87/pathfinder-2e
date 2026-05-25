---
type: creature
group: ["Plant"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Hippopotamus Topiary"
level: "11"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Plant"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+20; [[Low-Light Vision]], [[Scent]] (imprecise) 60 feet"
languages: "Muan (can't speak any language)"
skills:
  - name: Skills
    desc: "Athletics +23, Nature +21, Stealth +23"
abilityMods: ["+7", "+4", "+4", "-2", "+0", "+3"]
abilities_top:
  - name: "Branchlocation"
    desc: "The hippopotamus topiary can tap its branches together and use its hearing as a precise sense at the listed range."
  - name: "Absorb Water"
    desc: "When in water or exposed to a water effect, the hippopotamus loses its weakness to fire until the start of its next turn."
  - name: "Swamp Fever"
    desc: "**Saving Throw** DC 26 [[Fortitude]] save <br>  <br> **Onset** 1 day <br>  <br> **Stage 1** [[Sickened]] 1 (1 day) <br>  <br> **Stage 2** [[Sickened]] 2 (1 day) <br>  <br> **Stage 3** sickened 2 and 1d8 persistent,bleed damage (1 day) <br>  <br> **Stage 4** sickened 2, [[Drained]] 1, and 2d8 persistent,bleed damage (1 day) <br>  <br> **Stage 5** dead"
  - name: "Walk Through Plants"
    desc: "The hippopotamus topiary ignores difficult terrain caused by dense vegetation."
armorclass:
  - name: AC
    desc: "30; **Fort** +24, **Ref** +21, **Will** +18"
health:
  - name: HP
    desc: "220; **Immunities** bleed"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +22 (`pf2:1`), **Damage** 2d10+15 piercing plus [[Grab]] plus [[Swamp Fever]]"
  - name: "Melee strike"
    desc: "Hoof +22 (`pf2:1`), **Damage** 2d8+15 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Jaw Crush"
    desc: "`pf2:1` **Requirements** The hippopotamus topiary has a creature [[Grabbed]] <br>  <br> **Effect** It forcefully bites down on whatever is in its mouth, dealing 6d8 piercing damage with a DC 27 [[Reflex]] save. On a critical failure, creatures take 1d8 persistent,bleed damage."
  - name: "Pruning"
    desc: "`pf2:1` The hippopotamus topiary twists and contorts its shape, shedding branches and leaves as needed to change into a topiary of a Medium or smaller animal. Until the next time it acts, the topiary has an automatic result of 43 for Deception checks and DCs to appear as a mundane topiary."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

One of the rarest types of living topiaries is the hippopotamus. These large shrubs are formed from souls with larger-than-life personalities. While less agile and perceptive than smaller topiaries, they're much more aggressive and territorial. As such, they tend to live solitary lives around swamps and marshes, giving them plenty of water and vegetation to roam around in.

Topiaries are an extremely common sight across Golarion, especially within the gleaming and well-manicured lawns of nobility. Living topiaries develop from the death of a lone soul in an overgrown area of deep primal magic, with the soul exploding into the plants around it and causing them to grow together into the form of an animal, often influenced by the personality of the dying person. Once fully formed, the living topiary lacks their original memories; however, they're filled with the desire to protect the area they were formed in, driving off invaders and those who would do harm to the flora and fauna.

```statblock
creature: "Hippopotamus Topiary"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
