---
type: creature
group: ["Beast", "Couatl"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Quetz Coatl"
level: "10"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Beast"
trait_02: "Couatl"
trait_03: "Holy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+21; [[Darkvision]]"
languages: "Common, Empyrean, Sussuran, Utopian (Telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +16, Arcana +19, Athletics +19, Diplomacy +22, Nature +22, Occultism +19, Religion +22, Survival +16"
abilityMods: ["+7", "+3", "+5", "+6", "+5", "+5"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "At-Will Spells"
    desc: "The monster can cast its at-will spells any number of times without using up spell slots."
  - name: "Quetz Couatl Venom"
    desc: "To unholy creatures, this is a curse instead of a poison and deals spirit damage instead of poison damage <br>  <br> **Saving Throw** DC 29 [[Fortitude]] save; <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 2d6 poison damage and [[Enfeebled]] 1 (1 round) <br>  <br> **Stage 2** 2d8 poison damage, enfeebled 1, and [[Off Guard]] (1 round) <br>  <br> **Stage 3** 2d10 poison damage, [[Enfeebled]] 2, and off-guard (1 round)"
armorclass:
  - name: AC
    desc: "30; **Fort** +19, **Ref** +19, **Will** +21"
health:
  - name: HP
    desc: "175"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +23 (`pf2:1`) (holy, magical, unarmed), **Damage** 2d10+13 piercing plus [[Grab]] plus [[Quetz Couatl Venom]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 29, attack +21<br>**7th** [[Interplanar Teleport (Self Only)]]<br>**5th** [[Breath of Life]]<br>**4th** [[Divine Wrath]], [[Vapor Form]]<br>**3rd** [[Mind Reading]] (At Will)<br>**2nd** [[Cleanse Affliction]]<br>**1st** [[Charm]], [[Light]], [[Telekinetic Hand]], [[Vitality Lash]]"
abilities_bot:
  - name: "Greater Constrict"
    desc: "`pf2:1` @Damage[(2d10+7)[bludgeoning]], DC 29 [[Fortitude]] save <br>  <br> The monster deals the listed amount of damage to any number of creatures [[Grabbed]] or [[Restrained]] by it. Each of those creatures can attempt a basic Fortitude save with the listed DC. A creature that fails this save falls [[Unconscious]], and a creature that succeeds is then temporarily immune to falling unconscious from Greater Constrict for 1 minute."
  - name: "Radiant Wings"
    desc: "`pf2:2` The quetz coatl spreads their multicolored wings and radiant plumage. Each enemy in a @Template[emanation|distance:30] must attempt a DC 29 [[Will]] save. <br> - **Critical Success** The creature is unaffected and is temporarily immune to Radiant Wings for 24 hours. <br> - **Success** The creature is [[Dazzled]] for 1 round. <br> - **Failure** The creature is dazzled for 1 minute. <br> - **Critical Failure** As failure, plus if the creature is unholy, it is also [[Stunned]] 3."
  - name: "Wrap in Coils"
    desc: "`pf2:1` **Requirements** The quetz couatl has a Medium or smaller creature [[Grabbed]] or [[Restrained]] in its jaws <br>  <br> **Effect** The quetz couatl moves the creature into its coils, freeing its fangs to make attacks, then uses [[Greater Constrict]] against the creature. The quetz couatl can hold as many creatures in its coils as will fit in its space."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

These sacred feathered serpents tirelessly serve the powers of knowledge and justice. Some operate directly as messengers and intermediaries of the deities, while others operate independently in aiding the cause of righteousness. Either way, they watch over mortals and try to influence and aid them from the shadows, shifting from plane to plane to spread wisdom and healing where they are needed. Some quetz coatls are worshipped as divinities in remote or isolated societies, and while they do not encourage such veneration, they use the trust placed in them to foster peace and cooperation with others.

Quetz coatls are typically 10 to 20 feet long and weigh nearly a ton, with iridescent blue and green scales. Their glorious wings of rainbow-hued feathers span 15 feet. They are carnivorous, feeding on birds, mammals, and even the occasional malicious humanoid.

```statblock
creature: "Quetz Coatl"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
