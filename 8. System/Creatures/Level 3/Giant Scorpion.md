---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Giant Scorpion"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+9; [[Darkvision]], [[Tremorsense]] (imprecise) 60 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +11, Stealth +7"
abilityMods: ["+4", "+2", "+3", "-5", "+2", "-4"]
abilities_top:
  - name: "Giant Scorpion Venom"
    desc: "**Saving Throw** DC 18 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 1d10 poison damage and [[Enfeebled]] 1 (1 round) <br>  <br> **Stage 2** 2d10 poison damage and enfeebled 1 (1 round) <br>  <br> **Stage 3** 2d10 poison damage and [[Enfeebled]] 2 (1 round)"
armorclass:
  - name: AC
    desc: "18; **Fort** +12, **Ref** +9, **Will** +7"
health:
  - name: HP
    desc: "45"
abilities_mid:
  - name: "Reactive Strike (Stinger Only)"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Pincer +11 (`pf2:1`) (agile, reach 10 ft.), **Damage** 1d8+6 slashing plus [[Grab]]"
  - name: "Melee strike"
    desc: "Stinger +11 (`pf2:1`) (reach 10 ft.), **Damage** 1d6+6 piercing plus [[Giant Scorpion Venom]]"
spellcasting: []
abilities_bot:
  - name: "Constrict"
    desc: "`pf2:1` @Damage[(1d6+4)[bludgeoning]], DC 20 [[Fortitude]] save <br>  <br> The monster deals the listed amount of damage to any number of creatures [[Grabbed]] or [[Restrained]] by it. Each of those creatures can attempt a basic Fortitude save with the listed DC."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

These massive, terrifying arachnids are typically 8 feet long from head to the base of the tail. Giant scorpions are the favored pack animals and war beasts of various desert-dwelling creatures, particularly kholos. They are most commonly encountered in the wild, however. There they lair in mountainside caves or burrow beneath shallow layers of sand where they lie in wait for prey to wander near.

Chitinous scourges of deserts, forests, savannas, and badlands, scorpions are deadly arachnids with powerful pincers and a painful sting. Scorpions can be found in nearly every climate, where they hunt their prey with a mixture of patient stealth and raw strength. Most scorpions live in underground burrows, either as lone hunters or part of a larger colony. These arachnids are so feared and dangerous that in many cultures, they are treated as deities or dualistic symbols of both death and protection from said death.

```statblock
creature: "Giant Scorpion"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
