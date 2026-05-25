---
type: creature
group: ["Plant"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Mandragora"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Plant"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+11; [[Low-Light Vision]]"
languages: "Chthonian, Common"
skills:
  - name: Skills
    desc: "Acrobatics +10, Athletics +10, Stealth +12"
abilityMods: ["+2", "+5", "+3", "-1", "+2", "+0"]
abilities_top:
  - name: "Blood Scent"
    desc: "A mandragora can smell creatures with blood as an imprecise sense at a range of 30 feet, and it can smell demons, fey, and sorcerers with blood as a precise sense at a range of 30 feet."
  - name: "Mandragora Venom"
    desc: "**Saving Throw** DC 21 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 1d6 poison damage and [[Stupefied 1]] (1 round) <br>  <br> **Stage 2** 1d6 poison damage, [[Confused]], and [[Stupefied 1]] (1 round) <br>  <br> **Stage 3** 2d6 poison damage, [[Confused]], and [[Stupefied 1]] (1 round)"
armorclass:
  - name: AC
    desc: "21; **Fort** +11, **Ref** +13, **Will** +8"
health:
  - name: HP
    desc: "60; **Weaknesses** fire 5; **Resistances** bludgeoning 5, electricity 5"
abilities_mid:
  - name: "Vulnerability to Supernatural Darkness"
    desc: "Whenever a mandragora begins its turn in an area of magical darkness, it is [[Slowed]] 1 on that turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +14 (`pf2:1`) (finesse, unarmed), **Damage** 2d8+4 piercing plus [[Grab]]"
  - name: "Melee strike"
    desc: "Thorny Vine +14 (`pf2:1`) (agile, finesse, reach 10 ft.), **Damage** 2d4+4 slashing plus [[Mandragora Venom]]"
spellcasting: []
abilities_bot:
  - name: "Blood Drain"
    desc: "`pf2:1` **Requirements** The mandragora has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** The mandragora drains blood from the creature it has grabbed or restrained, dealing 2d6 piercing damage (DC 21 [[Fortitude]] save). If the creature is a demon, fey, or sorcerer, the mandragora gains temporary Hit Points equal to the damage dealt for 1 minute. A creature that takes any damage from having its blood drained by a mandragora is [[Drained]] 1 until it receives any kind or amount of healing."
  - name: "Piercing Shriek"
    desc: "`pf2:1` **Frequency** once per day <br>  <br> **Effect** The mandragora emits an unsettling shriek. Each non-mandragora creature within 30 feet must attempt a DC 23 [[Will]] save. <br> - **Critical Success** The creature is unaffected. <br> - **Success** The creature is [[Sickened]] 1. <br> - **Failure** The creature is [[Sickened]] 2. <br> - **Critical Failure** The creature is sickened 2 and [[Slowed]] 1. As long as the creature remains sickened, this slowed condition value can't be reduced below 1."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

A mandragora looks like a freshly pulled tuber that has grown into the malformed shape of a child with a grotesque face and hideously bloated body. These insidious little plants typically form when a mandrake root is watered with a demon's blood. Upon absorbing the otherworldly properties of the demon's blood, the root animates and is forced to seek out blood to feast from, lest it die of thirst.

Always famished and in search for sustenance, mandragoras live haunted, pained lives and perform vile and desperate acts to acquire the blood they crave. Though mandragoras prefer magically infused blood such as that of unicorns, fey, or sorcerers, and they can subsist on potions, alchemical bombs, and magical elixirs, they'll settle for the blood of non-magical creatures as a last resort. They find the flavor of mundane blood to be bland and bitter, and they don't blanch at voicing these complaints to the creatures on whom they feed.

While the typical mandragora is the size of a human child, some continue to grow and grow, even reaching sizes comparable to giants. Sometimes as they get larger, they form additional limbs or rudimentary faces, eventually transforming into truly hideous mockeries of the human form.

```statblock
creature: "Mandragora"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
