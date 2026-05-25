---
type: creature
group: ["Cold", "Giant"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Snow Oni"
level: "13"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Cold"
trait_02: "Giant"
trait_03: "Humanoid"
trait_04: "Oni"
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+26; [[Greater Darkvision]]"
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +24, Athletics +25, Deception +27"
abilityMods: ["+8", "+5", "+5", "+0", "+5", "+8"]
abilities_top:
  - name: "Snow Vision"
    desc: "Snow doesn't impair the snow oni's vision; they ignore [[Concealment]] from snowfall."
armorclass:
  - name: AC
    desc: "33; **Fort** +23, **Ref** +25, **Will** +21"
health:
  - name: HP
    desc: "290; **Immunities** cold; **Weaknesses** spirit 15"
abilities_mid:
  - name: "Bean Panic"
    desc: "Oni are curiously afraid of beans, especially as the seasons begin to change. If a creature Interacts to throw a handful of beans at the oni, the oni becomes [[Frightened]] 2. While frightened this way, their weakness to spirit damage is increased by 5. The oni then becomes immune to bean panic for 24 hours."
  - name: "Icy Deflection"
    desc: "`pf2:r` **Trigger** The snow oni is targeted by a ranged Strike or spell attack roll that doesn't have the fire trait <br>  <br> **Effect** The snow oni creates a reflective blockade of ice, gaining a +4 circumstance bonus to AC against the triggering attack roll. If the attack misses, the snow oni redirects the attack to another creature within 20 feet of the snow oni. The attacker rerolls the attack roll against the new target."
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +27 (`pf2:1`) (agile, magical, reach 10 ft., unarmed), **Damage** 2d8+16 bludgeoning plus 2d6 cold"
  - name: "Melee strike"
    desc: "Jaws +27 (`pf2:1`) (magical, reach 10 ft., unarmed), **Damage** 2d6+16 piercing plus 1d6 bleed"
  - name: "Ranged strike"
    desc: "Ice Dart +25 (`pf2:1`) (cold, magical, range 60 ft.), **Damage** 3d10+4 cold plus 1d6 spirit"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 31, attack +23<br>**2nd** [[Invisibility (At Will, Self Only)]]"
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` The snow oni can take on the appearance of any Medium or Large humanoid creature. This doesn't change their Speed or their attack and damage bonuses with their Strikes but might change the damage type their Strikes deal (typically to bludgeoning). <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Chilling Combo"
    desc: "`pf2:1` The snow oni makes two fist Strikes targeting the same creature. If they both hit, the target becomes [[Slowed]] 1 for 1 round."
  - name: "Falling Frozen Lightning"
    desc: "`pf2:2` The snow oni calls down a bolt of icy lightning, white as fallen snow. The bolt strikes a location within 60 feet, freezing the air into a cloud of snow that fills a @Template[burst|distance:20] and lasts for 1 minute. <br>  <br> All creatures within the snow become [[Concealed]], and all creatures outside the snow become concealed to creatures within it. A creature that enters the snow or begins its turn there takes @Damage[15[cold]|options:area-damage] damage, with a DC 33 [[Fortitude]] save."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Snow oni maintain their seething temperaments even in their icy homes. The isolation of their environment gives them trappings of asceticism, and many snow oni pursue physical perfection, reveling in the process of turning their bodies into powerful fighting machines. They are just as hedonistic and brutal as any of their brethren, however, and eager to indulge in warm baths, strong drink, and humanoid flesh.

Like many oni, snow oni possess a third eye in the center of their forehead. This eye gives snow oni a mystical sense that allows them to peer through even the thickest flurries of snow.

Oni are large, brutal creatures originating in Tian Xia who resemble humanoids with brightly colored skin, tusks, and horns. Though commonly mistaken for fiends, the first oni were originally kami, tutelary nature spirits. These kami suffered a terrible trauma, losing their sacred wards to dramatic disasters or the callousness of others, and as a result transformed into the violent creatures they are today. While some believe that oni can be spiritually placated through proper ritual worship that transforms them back into kami, many of these would-be saviors fall to oni's notorious brute strength, flesh-rending teeth, and command of storms.

Oni possess the ability to disguise themselves as other humanoids. They are rarely creative in their disguises, often choosing a specific appearance similar to their oni form and sticking with it. This simplicity catches many by surprise, however, as people assume oni are limited to a single alternate form, which is by no means the case.

```statblock
creature: "Snow Oni"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
