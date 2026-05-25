---
type: creature
group: ["Beast", "Couatl"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Mix Coatl"
level: "8"
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
    desc: "+19; [[Darkvision]]"
languages: "Common, Draconic, Empyrean (telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +15, Arcana +18, Diplomacy +20, Nature +21, Occultism +18, Society +16, Stealth +17, Survival +15"
abilityMods: ["+6", "+3", "+4", "+4", "+5", "+4"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Star Child"
    desc: "The mix couatl is difficult to discern against starry skies. The mix couatl can [[Hide]] in the air at night without  <br>  <br> > [!danger] Effect: Cover <br>  <br>  or being [[Concealed]]."
  - name: "Gift of Knowledge"
    desc: "When a mix coatl casts [[Rewrite Memory]] on a willing creature, the mix coatl can Sustain the spell to rewrite these memories for up to 60 continuous minutes. A mix coatl can grant knowledge of a particular skill to the target as part of the spell. The mix coatl chooses Engineering Lore, Farming Lore, Fishing Lore, Hunting Lore, or Mercantile Lore. The target becomes permanently trained in the chosen skill. A creature can benefit from Gift of Knowledge only once."
  - name: "Mix Coatl Venom"
    desc: "To unholy creatures, this is a curse instead of a poison and deals spirit damage instead of poison damage <br>  <br> **Saving Throw** DC 26 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 1d6 poison damage and [[Stupefied 1]] (1 round) <br>  <br> **Stage 2** 2d6 poison damage, [[Stunned]] 1, and stupefied 1 (1 round) <br>  <br> **Stage 3** 2d8 poison damage, stunned 1, and [[Stupefied 2]] (1 round) <br>  <br> Against unholy <br>  <br> **Saving Throw** DC 26 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 1d6 spirit damage and [[Stupefied 1]] (1 round) <br>  <br> **Stage 2** 2d6 spirit damage, [[Stunned]] 1, and stupefied 1 (1 round) <br>  <br> **Stage 3** 2d8 spirit damage, stunned 1, and [[Stupefied 2]] (1 round)"
armorclass:
  - name: AC
    desc: "27; **Fort** +14, **Ref** +15, **Will** +19"
health:
  - name: HP
    desc: "135"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +20 (`pf2:1`) (magical, unarmed), **Damage** 2d10+9 piercing plus [[Grab]] plus [[Mix Couatl Venom]]"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 26, attack +18<br>**7th** [[Interplanar Teleport (self only)]]<br>**3rd** [[Fireball]], [[Mind Reading]] (At Will), [[Speak with Plants]]<br>**2nd** [[Invisibility (self only)]], [[Speak with Animals]]<br>**1st** [[Create Water]], [[Guidance]], [[Heal]], [[Ignition]], [[Light]], [[Mending]], [[Stabilize]]"
abilities_bot:
  - name: "Constrict"
    desc: "`pf2:1` @Damage[(2d10+4)[bludgeoning]], DC 26 [[Fortitude]] save <br>  <br> The monster deals the listed amount of damage to any number of creatures [[Grabbed]] or [[Restrained]] by it. Each of those creatures can attempt a basic Fortitude save with the listed DC."
  - name: "Wrap in Coils"
    desc: "`pf2:1` **Requirements** The mix coatl has a Medium or smaller creature [[Grabbed]] or [[Restrained]] in their jaws <br>  <br> **Effect** The mix coatl moves the creature into their coils, freeing their jaws to make attacks, and then uses Constrict against the creature. The mix coatl can hold as many creatures in their coils as will fit in their space."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Mix coatls (pronounced "meesh") are guides to fledgling societies, providing fundamental information such as farming techniques, medicinal expertise, or more esoteric knowledge like the arcane arts.

Coatls are serpentine celestials who tirelessly help mortals reach their greatest potential all across the planes. Some serve benevolent deities as intermediaries, while others serve the cause of good as they see fit.

```statblock
creature: "Mix Coatl"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
