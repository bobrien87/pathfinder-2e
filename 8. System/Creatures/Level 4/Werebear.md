---
type: creature
group: ["Beast", "Human"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Werebear"
level: "4"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Beast"
trait_02: "Human"
trait_03: "Humanoid"
trait_04: "Werecreature"
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+11; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: "Common (Bear Empathy)"
skills:
  - name: Skills
    desc: "Athletics +12, Medicine +9, Nature +11, Stealth +11, Survival +11"
abilityMods: ["+5", "+2", "+4", "+1", "+3", "-1"]
abilities_top:
  - name: "Bear Empathy"
    desc: "The werebear can communicate with ursine creatures. <br>  <br> The werecreature can ask questions of, receive answers from, and use the Diplomacy skill with animals of its general kind."
  - name: "Curse of the Werebear"
    desc: "This curse affects only humanoids. <br>  <br> **Saving Throw** DC 18 [[Fortitude]] save <br>  <br> On each full moon, the cursed creature must succeed at another Fortitude save or turn into the same kind of werecreature until dawn. <br>  <br> The creature is under the GM's control and goes on a rampage for half the night before falling unconscious until dawn."
  - name: "Mauler"
    desc: "The werebear gains a +2 circumstance bonus to damage rolls against creatures it has [[Grabbed]]."
  - name: "Moon Frenzy"
    desc: "When a full moon appears in the night sky, the werecreature must enter hybrid form, can't Change Shape thereafter, becomes one size larger, increases its reach by 5 feet, and increases the damage of its jaws by 2. <br>  <br> When the moon sets or the sun rises, the werecreature returns to humanoid form and is [[Fatigued]] for 2d4 hours. <br>  <br> > [!danger] Effect: Moon Frenzy"
armorclass:
  - name: AC
    desc: "23; **Fort** +12, **Ref** +10, **Will** +10"
health:
  - name: HP
    desc: "75; **Weaknesses** silver 5"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Greataxe +13 (`pf2:1`) (reach 10 ft., sweep), **Damage** 1d12+7 slashing"
  - name: "Melee strike"
    desc: "Hatchet +13 (`pf2:1`) (agile, sweep), **Damage** 1d6+7 slashing"
  - name: "Melee strike"
    desc: "Hatchet +10 (`pf2:1`) (agile, sweep, thrown 10), **Damage** 1d6+7 slashing"
spellcasting: []
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` - **Human** <br>  <br> - **Size** Medium <br>  <br> - **Melee** fist +13 **Damage** 1d4+7 <br>  <br> - **Grizzly Bear** <br>  <br> - **Speed** 35 feet <br>  <br> The werecreature changes into its humanoid, hybrid, or animal shape. Each shape has a specific, persistent appearance. A true werecreature's natural form is its hybrid shape. <br>  <br> In humanoid shape, the werecreature uses its original humanoid size, loses its jaws and claws Strikes, and gains a melee fist Strike that deals bludgeoning damage equal to the slashing damage dealt by its claw. <br>  <br> In animal shape, its Speed and size change to that of the animal, it gains any special Strike effects of the animal that it didn't already have (such as Grab), and it loses its weapon Strikes. <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Hunt Prey"
    desc: "`pf2:1` The werebear designates a single creature they can see and hear, or one they're Tracking, as their prey. The werebear gains a +2 circumstance bonus to Perception checks when they [[Seek]] their prey and to Survival checks when they [[Track]] their prey. The first time the werebear hits the designated prey in a round, they deal an additional 1d8 precision damage. These effects last until the werebear uses Hunt Prey again."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Unwavering conviction fills a werebear during their transformations. This can drive them zealously into noble causes, but it can also make them ruthless, violent, and single-minded. Alliances can fall from a werebear's mind as their bestial temper overcomes them and their goal overwhelms all. As a result, werebears are loners, rarely even living together as families longer than necessary. As long as there is nothing around to threaten it or the natural area it protects (typically a forest), a werebear in its animal form is generally content to forage and sleep away the night.

Werecreatures are humanoids doomed to transform into animals and animalhumanoid hybrids under the light of the full moon. These shapechanging creatures are the result of an ancient primal curse that they can, in turn, transmit through their own bites. Their ability to lurk unseen in the wilds as well as among people, combined with the contagiousness of their condition, makes werecreatures a perennial cause of panicked suspicion.

```statblock
creature: "Werebear"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
