---
type: creature
group: ["Beast", "Human"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Werewolf"
level: "3"
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
    desc: "+9; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: "Common (Wolf Empathy)"
skills:
  - name: Skills
    desc: "Acrobatics +7, Athletics +9, Survival +10"
abilityMods: ["+4", "+2", "+2", "-1", "+2", "+1"]
abilities_top:
  - name: "Wolf Empathy"
    desc: "The werewolf can communicate with canine creatures. <br>  <br> The werecreature can ask questions of, receive answers from, and use the Diplomacy skill with animals of its general kind."
  - name: "Curse of the Werewolf"
    desc: "This curse affects only humanoids. <br>  <br> **Saving Throw** DC 17 [[Fortitude]] save <br>  <br> On each full moon, the cursed creature must succeed at another Fortitude save or turn into the same kind of werecreature until dawn. <br>  <br> The creature is under the GM's control and goes on a rampage for half the night before falling unconscious until dawn."
  - name: "Moon Frenzy"
    desc: "When a full moon appears in the night sky, the werecreature must enter hybrid form, can't Change Shape thereafter, becomes one size larger, increases its reach by 5 feet, and increases the damage of its jaws by 2. <br>  <br> When the moon sets or the sun rises, the werecreature returns to humanoid form and is [[Fatigued]] for 2d4 hours. <br>  <br> > [!danger] Effect: Moon Frenzy"
  - name: "Pack Attack"
    desc: "The werewolf's Strikes deal 1d6 extra damage to creatures within reach of at least two of the werewolf's allies."
armorclass:
  - name: AC
    desc: "17; **Fort** +11, **Ref** +9, **Will** +7"
health:
  - name: HP
    desc: "63; **Weaknesses** silver 5"
abilities_mid:
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Battle Axe +11 (`pf2:1`) (sweep), **Damage** 1d8+8 slashing"
  - name: "Ranged strike"
    desc: "Composite Shortbow +9 (`pf2:1`) (deadly d10, reload 0, range 60 ft.), **Damage** 1d6+4 piercing"
spellcasting: []
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` - **Human** <br>  <br> - **Melee** fist +11 **Damage** 1d4+8 <br>  <br> - **Animal** <br>  <br> - **Speed** 40 feet <br>  <br> - **Melee** jaws with [[Knockdown]] <br>  <br> The werecreature changes into its humanoid, hybrid, or animal shape. Each shape has a specific, persistent appearance. A true werecreature's natural form is its hybrid shape. <br>  <br> In humanoid shape, the werecreature uses its original humanoid size, loses its jaws and claws Strikes, and gains a melee fist Strike that deals bludgeoning damage equal to the slashing damage dealt by its claw. <br>  <br> In animal shape, its Speed and size change to that of the animal, it gains any special Strike effects of the animal that it didn't already have (such as Grab), and it loses its weapon Strikes. <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Knockdown (Animal Shape)"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Knockdown in its damage entry <br>  <br> **Effect** The monster attempts to `act trip` the creature. This attempt neither applies nor counts toward the monster's multiple attack penalty."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The curse of the werewolf—known as lycanthropy to many—instills in its carriers the hungry bloodlust and predatory instincts of the wolf. Werewolves tend to dwell on the fringes of society or in small settlements where, in their humanoid forms, they work as laborers, hunters, farmers, or trappers. At night, however, these same villagers transform into violent killers and sadistic stalkers who prey on their neighbors. Werewolves are the quintessential werecreature, and the first that comes to mind when most people speak of such beings.

Although most werewolves hide their curse by adopting solitary lifestyles, some retain the pack mentality of true wolves. A small group of such werewolves typically forms a family-like pack, with the eldest or most powerful werewolf serving as the leader. New pack mates are hand-chosen and inculcated into the family as its influence grows.

Werecreatures are humanoids doomed to transform into animals and animalhumanoid hybrids under the light of the full moon. These shapechanging creatures are the result of an ancient primal curse that they can, in turn, transmit through their own bites. Their ability to lurk unseen in the wilds as well as among people, combined with the contagiousness of their condition, makes werecreatures a perennial cause of panicked suspicion.

```statblock
creature: "Werewolf"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
