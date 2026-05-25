---
type: creature
group: ["Plant"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Dezullon"
level: "10"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Plant"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+18; [[Low-Light Vision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +21, Athletics +19, Stealth +21"
abilityMods: ["+5", "+7", "+3", "-4", "+2", "-1"]
abilities_top:
  - name: "Amnesia Venom"
    desc: "**Saving Throw** DC 29 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** [[Off Guard]] (1 round) <br>  <br> **Stage 2** off-guard and [[Clumsy]] 1 (1 round) <br>  <br> **Stage 3** [[Confused]], off-guard, and [[Clumsy]] 2 (1 round) <br>  <br> **Stage 4** as Stage 3 and permanently forget the last hour (1 round)"
armorclass:
  - name: AC
    desc: "30; **Fort** +17, **Ref** +21, **Will** +16"
health:
  - name: HP
    desc: "130; regeneration 15 (deactivated by fire); **Resistances** acid 20"
abilities_mid:
  - name: "Regeneration 15 (Deactivated by Fire)"
    desc: "This monster regains the listed number of Hit Points each round at the beginning of its turn. Its [[Dying]] condition never increases beyond Dying 3 as long as its regeneration is active. However, if it takes damage of a type listed in the regeneration entry, its regeneration deactivates until the end of its next turn. Deactivate the regeneration before applying any damage of a listed type, since that damage might kill the monster by bringing it to Dying 4."
  - name: "Stench"
    desc: "30 feet. DC 27 [[Fortitude]] save <br>  <br> A creature entering the aura or starting its turn in the area must succeed at a Fortitude save or become [[Sickened]] 1 (plus [[Slowed]] 1 as long as it's sickened on a critical failure). A creature that succeeds at its save or recovers from being sickened is temporarily immune to all stench auras for 1 minute."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Vine +21 (`pf2:1`) (acid, agile), **Damage** 3d6+8 bludgeoning plus 3d6 acid plus [[Grab]]"
  - name: "Ranged strike"
    desc: "Acid Glob +23 (`pf2:1`) (acid), **Damage** 4d8 acid plus [[Amnesia Venom]]"
spellcasting: []
abilities_bot:
  - name: "Constrict"
    desc: "`pf2:1` @Damage[(2d6+2)[bludgeoning]], DC 29 [[Fortitude]] save <br>  <br> The monster deals the listed amount of damage to any number of creatures [[Grabbed]] or [[Restrained]] by it. Each of those creatures can attempt a basic Fortitude save with the listed DC."
  - name: "Root"
    desc: "`pf2:1` Until the next time it acts, the dezullon appears to be a normal pitcher plant. It has an automatic result of 41 (44 in forests or swamps) on Deception checks and DCs to pass as a non-creature plant."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Dezullons are dangerous, carnivorous pitcher plants that dwell in forested regions with thick canopies or deep in marshes where few other plants can grow. They hunt for meat along the forest's understory when not sunning themselves in the boughs above. Dezullons are smart enough to notice that some creatures are attracted by shiny things, and sometimes use such objects to set up ambushes. To assume that the dezullon's ambulations are slow simply because the creature has a root structure is a foolish mistake; many an adventurer has been crushed to death by this surprisingly agile plant. In addition, dezullons are expert climbers, which makes escaping them in a forest even more difficult.

A hungry dezullon keeps prey off-balance by spilling its putrid, psychoactive digestive juices from its central pitcher. In addition to being highly acidic, the enzymes in a dezullon's digestive tract, once expelled, inflicts powerful hallucinations and amnesia. This secondary effect makes dezullons highly sought after in some circles, including avid drug users, experimental doctors, and criminals who deal in poisons.

Attempts to cultivate dezullons typically end in disaster, although druids and fey who can communicate with plants have found measured success. Meanwhile, horned dragons looking for breakthroughs in their research or groups of marsh giants seeking visions from their esoteric gods trust their power to hunt and overwhelm the plants.

Many varieties of dezullon exist, including lumbering giants of incredible size, dezullons with tiny, cup-shaped pitchers that proliferate along lengths of creeping ivy like suckers on a squid's tentacles, and a variant with hundreds of blood-red, razor-sharp leaves that protrude from the inside of their pitchers like a leech's teeth. This latter variety is especially dangerous, since the leaves can all but eviscerate creatures that become trapped inside their pitchers.

```statblock
creature: "Dezullon"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
