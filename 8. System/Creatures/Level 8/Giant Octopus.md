---
type: creature
group: ["Animal", "Aquatic"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Giant Octopus"
level: "8"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Animal"
trait_02: "Aquatic"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+15; [[Low-Light Vision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +17, Athletics +20, Stealth +17"
abilityMods: ["+6", "+3", "+4", "-4", "+3", "-2"]
abilities_top:
  - name: "Compression"
    desc: "A giant octopus can move through a gap at least 2 feet wide without Squeezing, and can [[Squeeze]] through a gap at least 1 foot wide."
  - name: "Giant Octopus Venom"
    desc: "**Saving Throw** DC 26 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 2d6 poison damage and [[Off Guard]] (1 round) <br>  <br> **Stage 2** 2d6 poison damage, [[Clumsy]] 1, and off-guard (1 round) <br>  <br> **Stage 3** 2d6 poison damage, [[Clumsy]] 2, and off-guard (1 round)"
armorclass:
  - name: AC
    desc: "27; **Fort** +16, **Ref** +17, **Will** +15"
health:
  - name: HP
    desc: "135; **Resistances** cold 10"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Arm +20 (`pf2:1`) (agile, reach 15 ft.), **Damage** 2d8+9 bludgeoning plus [[Grab]]"
  - name: "Melee strike"
    desc: "Beak +20 (`pf2:1`) (unarmed), **Damage** 2d8+9 piercing plus [[Giant Octopus Venom]]"
spellcasting: []
abilities_bot:
  - name: "Constrict"
    desc: "`pf2:1` @Damage[(1d8+9)[bludgeoning]], DC 26 [[Fortitude]] save <br>  <br> The monster deals the listed amount of damage to any number of creatures [[Grabbed]] or [[Restrained]] by it. Each of those creatures can attempt a basic Fortitude save with the listed DC."
  - name: "Ink Cloud"
    desc: "`pf2:1` The octopus emits a cloud of black ink in a @Template[emanation|distance:30]. This cloud has no effect outside of water. Creatures inside the cloud are [[Undetected]] and can't use their sense of smell. The cloud dissipates after 1 minute. <br>  <br> The octopus can't use Ink Cloud again for 2d6 rounds."
  - name: "Jet"
    desc: "`pf2:2` The octopus moves up to 200 feet in a straight line through the water without triggering reactions."
  - name: "Writhing Arms"
    desc: "`pf2:2` The giant octopus makes up to four Strikes with different arms, each against a different target. Each attack counts separately for the octopus's multiple attack penalty, but the penalty doesn't increase the until the octopus has made all the attacks. <br>  <br> If the octopus subsequently uses the [[Grab]] action, it can Grab any number of creatures it hit with Writhing Arms."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Giant octopuses are found in the heart of deep, dark oceans. Clever and adaptable, they hunt and devour all manner of animals. Despite growing up to 16 feet long, a giant octopus can compress its body to squeeze through small gaps as long as there's room for its beak.

Giant octopuses favor shipwrecks, coral reefs, or underwater caverns as lairs, where they can take advantage of narrow confines for protection. Like their smaller kin, they're fond of adorning and decorating their lairs with found objects—many of which, in the giant octopus's case, are also magical weapons, shields, or works of art salvaged from sunken ships or fallen adventurers.

```statblock
creature: "Giant Octopus"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
