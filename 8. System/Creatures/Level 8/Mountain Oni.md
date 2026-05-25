---
type: creature
group: ["Giant", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Mountain Oni"
level: "8"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Giant"
trait_02: "Humanoid"
trait_03: "Oni"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+17; [[Darkvision]]"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +16, Deception +18, Intimidation +18, Survival +17"
abilityMods: ["+6", "+3", "+4", "+0", "+3", "+4"]
abilities_top: []
armorclass:
  - name: AC
    desc: "26; **Fort** +18, **Ref** +15, **Will** +14"
health:
  - name: HP
    desc: "165; **Weaknesses** spirit 10"
abilities_mid:
  - name: "Bean Panic"
    desc: "Oni are curiously afraid of beans, especially as the seasons begin to change. If a creature Interacts to throw a handful of beans at the oni, the oni becomes [[Frightened]] 2. While frightened this way, their weakness to spirit damage is increased by 5. The oni then becomes immune to bean panic for 24 hours."
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +20 (`pf2:1`) (magical, reach 10 ft., unarmed), **Damage** 2d6+9 piercing plus 1d6 bleed"
  - name: "Melee strike"
    desc: "Tetsubo +21 (`pf2:1`) (magical, razing, reach 10 ft., shove, sweep), **Damage** 2d10+9 bludgeoning"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 25, attack +17<br>**2nd** [[Invisibility (At Will, Self Only)]]"
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` The mountain oni can take on the appearance of any Medium or Large humanoid creature. This doesn't change their Speed or their attack and damage bonuses with their Strikes but might change the damage type their Strikes deal (typically to bludgeoning). <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Thundering Iron"
    desc: "`pf2:2` The oni lifts their tetsubo and brings it down in a deafening peal. They make a tetsubo Strike. On a success, the target takes an additional 1d10 sonic damage. <br>  <br> Each creature in a @Template[emanation|distance:10] around the target, other than the oni, take this damage as well and is pushed 5 feet away from the target."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Mountain oni are the most common oni and often considered the least sophisticated. While other oni might have a stronger connection to the spiritual world, mountain oni have little interest in anything beyond satisfying their relentless appetites. Sloth and gluttony are common vices among mountain oni, which can allow them to coexist with nearby villages so long as they're well fed, but more ambitious mountain oni can often be found leading ogre war parties or orchestrating violent bandit raids. It's rare for mountain oni to live solitary existences, but those who do prefer to maraud the countryside or exploit villages and hoard the spoils for themselves.

Oni are large, brutal creatures originating in Tian Xia who resemble humanoids with brightly colored skin, tusks, and horns. Though commonly mistaken for fiends, the first oni were originally kami, tutelary nature spirits. These kami suffered a terrible trauma, losing their sacred wards to dramatic disasters or the callousness of others, and as a result transformed into the violent creatures they are today. While some believe that oni can be spiritually placated through proper ritual worship that transforms them back into kami, many of these would-be saviors fall to oni's notorious brute strength, flesh-rending teeth, and command of storms.

Oni possess the ability to disguise themselves as other humanoids. They are rarely creative in their disguises, often choosing a specific appearance similar to their oni form and sticking with it. This simplicity catches many by surprise, however, as people assume oni are limited to a single alternate form, which is by no means the case.

```statblock
creature: "Mountain Oni"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
