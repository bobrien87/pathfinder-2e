---
type: creature
group: ["Aquatic", "Elemental"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Quatoid"
level: "7"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Aquatic"
trait_02: "Elemental"
trait_03: "Water"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+18; [[Darkvision]]"
languages: "Common, Thalassic"
skills:
  - name: Skills
    desc: "Athletics +15, Diplomacy +12, Occultism +17, Society +17, Stealth +13, Elemental Lore +17"
abilityMods: ["+4", "+2", "+0", "+4", "+3", "+1"]
abilities_top:
  - name: "At-Will Spells"
    desc: "The monster can cast its at-will spells any number of times without using up spell slots."
armorclass:
  - name: AC
    desc: "25; **Fort** +13, **Ref** +15, **Will** +18"
health:
  - name: HP
    desc: "120; **Immunities** bleed, paralyzed, poison, sleep; **Resistances** bludgeoning 5, fire 5"
abilities_mid:
  - name: "Calming Bioluminescence"
    desc: "30 feet. <br>  <br> The aura sheds dim light. Creatures in the emanation gain a +2 circumstance bonus to saving throws against emotion effects. The quatoid can activate or deactivate its calming bioluminescence as a single action, which has the concentrate trait. <br>  <br> > [!danger] Effect: Calming Bioluminescence"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Tentacle +16 (`pf2:1`) (reach 10 ft., unarmed), **Damage** 2d12+6 bludgeoning plus [[Grab]]"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 27, attack +17<br>**1st** [[Hydraulic Push]] (At Will)"
abilities_bot:
  - name: "Constrict"
    desc: "`pf2:1` @Damage[(1d12+6)[bludgeoning]], DC 25 [[Fortitude]] save <br>  <br> The monster deals the listed amount of damage to any number of creatures [[Grabbed]] or [[Restrained]] by it. Each of those creatures can attempt a basic Fortitude save with the listed DC."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Quatoids are peculiar elementals native to the Plane of Water that resemble four-tentacled octopuses with eerily humanoid faces on their mantles. Mysterious even to other elementals, quatoids nevertheless respond to mortal summons. They assist these mortals in combat but seem to prefer offering calm advice, looking for alternate solutions even in the midst of bloody conflict.

With the return of their elemental lord from her long imprisonment, quatoids are slowly becoming more active on the Plane of Water. However, much of their activity still seems to be centered on the mortal realm.

Water elementals can be very destructive, but often not intentionally so; just as water can bring life to mortals in need, its waves can pound shores and rains can flood cities. Water elementals are similarly difficult to predict.

```statblock
creature: "Quatoid"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
