---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Giant Monitor Lizard"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+7; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +6, Athletics +9, Stealth +6"
abilityMods: ["+3", "+2", "+3", "-4", "+1", "-2"]
abilities_top:
  - name: "Monitor Lizard Venom"
    desc: "**Saving Throw** DC 17 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** [[Enfeebled]] 1 (1 round) <br>  <br> **Stage 2** 1d6 poison damage and [[Enfeebled]] 2 (1 round)"
armorclass:
  - name: AC
    desc: "18; **Fort** +9, **Ref** +8, **Will** +5"
health:
  - name: HP
    desc: "36"
abilities_mid:
  - name: "Gnashing Grip"
    desc: "`pf2:r` **Trigger** A creature [[Grabbed]] by the giant monitor lizard's jaws fails a check to [[Escape]]. <br>  <br> **Effect** The giant monitor lizard's jaws deal 1d6 piercing damage and the triggering creature is exposed to monitor lizard venom."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +11 (`pf2:1`) (unarmed), **Damage** 1d10+3 piercing plus [[Grab]] plus [[Monitor Lizard Venom]]"
spellcasting: []
abilities_bot:
  - name: "Lurching Charge"
    desc: "`pf2:2` The giant monitor lizard Strides twice and then makes a jaws Strike. If the lizard moved at least 20 feet away from its starting position, it gains a +2 circumstance bonus to this attack roll."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Large and seemingly ponderous, a monitor lizard is a deceptively swift and ruthless predator. It ambushes its prey by rushing out from cover and biting the target with its powerful jaws. A giant monitor lizard's saliva is venomous, allowing it to bring down prey larger than it can easily haul away in its jaws. Giant monitor lizards grow up to 14 feet long, including their long tails, and they weigh about 350 pounds. Their bodies are normally dark brown with patches of yellow or green.

When nesting, a giant monitor lizard digs a deep burrow to hide in. The burrow serves as both a safe haven and a location from which the lizard can ambush larger prey such as deer, boars, or even humanoids. A giant monitor lizard can consume nearly its own body weight in a single meal, and its loosely articulated jaws allow it to swallow surprisingly large prey.

Lizards have a wide range of appearances and abilities, but most share a basic reptilian shape—long tails, wide toothy mouths, and four legs. While a few species are capable of movement on two legs for short periods of time, most are strictly quadrupedal. The three species presented here represent the most common and well-known of the larger species.

```statblock
creature: "Giant Monitor Lizard"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
