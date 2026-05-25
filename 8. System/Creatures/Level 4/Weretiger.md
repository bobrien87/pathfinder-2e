---
type: creature
group: ["Beast", "Human"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Weretiger"
level: "4"
rare_01: "Common"
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
languages: "Common (Tiger Empathy)"
skills:
  - name: Skills
    desc: "Acrobatics +11, Athletics +12, Deception +7, Society +10, Stealth +11"
abilityMods: ["+4", "+3", "+3", "+0", "+3", "-1"]
abilities_top:
  - name: "Tiger Empathy"
    desc: "The weretiger can communicate with felines. <br>  <br> The werecreature can ask questions of, receive answers from, and use the Diplomacy skill with animals of its general kind."
  - name: "Curse of the Weretiger"
    desc: "This curse affects only humanoids. <br>  <br> **Saving Throw** DC 21 [[Fortitude]] save <br>  <br> On each full moon, the cursed creature must succeed at another Fortitude save or turn into the same kind of werecreature until dawn. <br>  <br> The creature is under the GM's control and goes on a rampage for half the night before falling unconscious until dawn."
  - name: "Moon Frenzy"
    desc: "When a full moon appears in the night sky, the werecreature must enter hybrid form, can't Change Shape thereafter, becomes one size larger, increases its reach by 5 feet, and increases the damage of its jaws by 2. <br>  <br> When the moon sets or the sun rises, the werecreature returns to humanoid form and is [[Fatigued]] for 2d4 hours. <br>  <br> > [!danger] Effect: Moon Frenzy"
armorclass:
  - name: AC
    desc: "21; **Fort** +11, **Ref** +13, **Will** +9"
health:
  - name: HP
    desc: "75; **Weaknesses** silver 5"
abilities_mid:
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks: []
spellcasting: []
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` - **Human**- **Melee** fist +14 **Damage** 1d4+7 <br>  <br> - **Animal**- **Speed** 30 feet <br> - Wrestle <br>  <br> The werecreature changes into its humanoid, hybrid, or animal shape. Each shape has a specific, persistent appearance. A true werecreature's natural form is its hybrid shape. <br>  <br> In humanoid shape, the werecreature uses its original humanoid size, loses its jaws and claws Strikes, and gains a melee fist Strike that deals bludgeoning damage equal to the slashing damage dealt by its claw. <br>  <br> In animal shape, its Speed and size change to that of the animal, it gains any special Strike effects of the animal that it didn't already have (such as Grab), and it loses its weapon Strikes. <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Pounce"
    desc: "`pf2:1` The weretiger Strides and makes a Strike at the end of that movement. If the weretiger began this action [[Hidden]], they remain hidden until after this ability's Strike."
  - name: "Rend"
    desc: "`pf2:1` Claw <br>  <br> A Rend entry lists a Strike the monster has. <br>  <br> **Requirements** The monster hit the same enemy with two consecutive Strikes of the listed type in the same round. <br>  <br> **Effect** The monster automatically deals that Strike's damage again to the enemy."
  - name: "Wrestle"
    desc: "`pf2:1` The weretiger makes a claw Strike against a creature it is [[Grabbing]]. If the attack hits, that creature is knocked [[Prone]]."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

These ferocious werecreatures stalk prey with the cunning and skill of a true apex predator. Weretigers typically view all life as a potential meal. Powerful nocturnal hunters with excellent senses that help them ambush prey, weretigers are adaptable to an extreme range of environments. However, weretigers living in densely populated cities (potentially as courtesans, assassins, or guild leaders) often struggle to suppress their killer instincts, becoming overwhelmed by the urge to hunt.

Werecreatures are humanoids doomed to transform into animals and animalhumanoid hybrids under the light of the full moon. These shapechanging creatures are the result of an ancient primal curse that they can, in turn, transmit through their own bites. Their ability to lurk unseen in the wilds as well as among people, combined with the contagiousness of their condition, makes werecreatures a perennial cause of panicked suspicion.

```statblock
creature: "Weretiger"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
