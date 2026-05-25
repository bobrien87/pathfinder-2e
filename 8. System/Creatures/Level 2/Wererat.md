---
type: creature
group: ["Beast", "Human"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Wererat"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Beast"
trait_02: "Human"
trait_03: "Humanoid"
trait_04: "Werecreature"
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+8; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: "Common (Rat Empathy)"
skills:
  - name: Skills
    desc: "Acrobatics +8, Athletics +6, Deception +5, Society +4, Stealth +8"
abilityMods: ["+2", "+4", "+2", "+0", "+2", "+1"]
abilities_top:
  - name: "Rat Empathy"
    desc: "The wererat can communicate with rodents. <br>  <br> The werecreature can ask questions of, receive answers from, and use the Diplomacy skill with animals of its general kind."
  - name: "Curse of the Wererat"
    desc: "This curse affects only humanoids. <br>  <br> **Saving Throw** DC 15 [[Fortitude]] save <br>  <br> On each full moon, the cursed creature must succeed at another Fortitude save or turn into the same kind of werecreature until dawn. <br>  <br> The creature is under the GM's control and goes on a rampage for half the night before falling unconscious until dawn."
  - name: "Moon Frenzy"
    desc: "When a full moon appears in the night sky, the werecreature must enter hybrid form, can't Change Shape thereafter, becomes one size larger, increases its reach by 5 feet, and increases the damage of its jaws by 2. <br>  <br> When the moon sets or the sun rises, the werecreature returns to humanoid form and is [[Fatigued]] for 2d4 hours. <br>  <br> > [!danger] Effect: Moon Frenzy"
  - name: "Sneak Attack"
    desc: "The wererat deals 1d6 extra precision damage to [[Off Guard]] creatures."
armorclass:
  - name: AC
    desc: "19; **Fort** +6, **Ref** +10, **Will** +8"
health:
  - name: HP
    desc: "45; **Weaknesses** silver 5"
abilities_mid:
  - name: "Nimble Dodge"
    desc: "`pf2:r` **Trigger** A creature targets the wererat with an attack and the wererat can see the attacker; <br>  <br> **Effect** The wererat gains a +2 circumstance bonus to AC against the triggering attack."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Shortsword +10 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d6+4 piercing"
  - name: "Ranged strike"
    desc: "Hand Crossbow +10 (`pf2:1`) (reload 1, range 60 ft.), **Damage** 1d6 piercing"
spellcasting: []
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` - **Human** <br>  <br> - **Melee** fist +10 **Damage** 1d4+2 bludgeoning <br>  <br> - **Rat** <br>  <br> - **Size** small <br>  <br> - **Speed** 30 feet, climb 10 feet <br>  <br> The werecreature changes into its humanoid, hybrid, or animal shape. Each shape has a specific, persistent appearance. A true werecreature's natural form is its hybrid shape. <br>  <br> In humanoid shape, the werecreature uses its original humanoid size, loses its jaws and claws Strikes, and gains a melee fist Strike that deals bludgeoning damage equal to the slashing damage dealt by its claw. <br>  <br> In animal shape, its Speed and size change to that of the animal, it gains any special Strike effects of the animal that it didn't already have (such as Grab), and it loses its weapon Strikes. <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Wererats tend to be selfishly opportunistic, avaricious, and paranoid as a result of their curse. Because wererats typically dwell in metropolitan areas where they can hide in plain sight, practically any city goer could be a wererat in disguise—from the quiet shopkeep to the city's criminal mastermind. The bustle of crowds and countless rat holes make ghettos and shantytowns favored homes for wererats, especially since in these poorer districts the wererat can kill out of greed or fear with little chance of the authorities noticing. In some cities, wererats operate entire thieves' guilds or organized crime rings, and membership requires willfully submitting to the wererat's cursed bite. Wererats look very similar to ratfolk when in hybrid form, apart from potential differences in size, but ratfolk have no love for wererats.

Werecreatures are humanoids doomed to transform into animals and animalhumanoid hybrids under the light of the full moon. These shapechanging creatures are the result of an ancient primal curse that they can, in turn, transmit through their own bites. Their ability to lurk unseen in the wilds as well as among people, combined with the contagiousness of their condition, makes werecreatures a perennial cause of panicked suspicion.

```statblock
creature: "Wererat"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
