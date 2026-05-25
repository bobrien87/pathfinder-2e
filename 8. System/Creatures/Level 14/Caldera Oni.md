---
type: creature
group: ["Fire", "Giant"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Caldera Oni"
level: "14"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Fire"
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
    desc: "Acrobatics +23, Athletics +27, Crafting +25, Deception +27, Intimidation +27"
abilityMods: ["+8", "+6", "+6", "+0", "+6", "+8"]
abilities_top: []
armorclass:
  - name: AC
    desc: "35; **Fort** +28, **Ref** +25, **Will** +23"
health:
  - name: HP
    desc: "315; **Immunities** fire; **Weaknesses** spirit 15"
abilities_mid:
  - name: "Bean Panic"
    desc: "Oni are curiously afraid of beans, especially as the seasons begin to change. If a creature Interacts to throw a handful of beans at the oni, the oni becomes [[Frightened]] 2. While frightened this way, their weakness to spirit damage is increased by 5. The oni then becomes immune to bean panic for 24 hours."
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Stoke the Volcano"
    desc: "When the caldera oni is critically hit, the flames of anger grow within them. They recharge their choice of Ash Form or Dance of Burning War."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Katana +30 (`pf2:1`) (deadly d8, magical, two hand d10, versatile p), **Damage** 2d6+14 slashing plus 2d6 fire"
  - name: "Melee strike"
    desc: "Jaws +28 (`pf2:1`) (magical, reach 10 ft., unarmed), **Damage** 2d6+14 piercing plus 1d8 bleed"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 34, attack +26<br>**2nd** [[Invisibility (At Will, Self Only)]]"
abilities_bot:
  - name: "Ash Form"
    desc: "`pf2:2` **Frequency** once per minute <br>  <br> **Effect** The caldera oni transforms into a cloud of sparking volcanic ash and then Flies. This movement doesn't trigger reactions, and the caldera oni can move through small gaps and spaces occupied by other creatures. <br>  <br> The caldera oni then returns to its physical form, affected by a 4th-rank [[Enlarge]] spell with a duration of 1d4 rounds."
  - name: "Change Shape"
    desc: "`pf2:1` The caldera oni can take on the appearance of any Medium or Large humanoid creature. This doesn't change their Speed or their attack and damage bonuses with their Strikes but might change the damage type their Strikes deal (typically to bludgeoning). <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Dance of Burning War"
    desc: "`pf2:3` **Frequency** once per minute <br>  <br> **Effect** The oni's heat becomes overwhelming, causing them to breathe out superheated ash and dance across the battlefield. The caldera oni Strides, then makes a melee Strike. If the Strike hits, the oni can Stride again and Strike again, repeating this until they have either missed with a Strike or made three Strikes total. <br>  <br> The oni then finishes the dance by calling down volcanic lightning through the cloud of ash. Each creature hit by a Strike during the dance takes @Damage[3d6[fire],3d6[electricity]]{3d6 fire damage and 3d6 electricity damage} with a DC 34 [[Reflex]] save."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

As hot-blooded as the lava that floods their homes, caldera oni have an incredible appetite for the thrill of war. While they engage in battle to conquer and control others, caldera oni also love the thrill of combat, fighting for the sheer joy of it. Presenting a caldera oni with a true challenge can potentially earn their mercy and an offer to serve at their side.

Oni are large, brutal creatures originating in Tian Xia who resemble humanoids with brightly colored skin, tusks, and horns. Though commonly mistaken for fiends, the first oni were originally kami, tutelary nature spirits. These kami suffered a terrible trauma, losing their sacred wards to dramatic disasters or the callousness of others, and as a result transformed into the violent creatures they are today. While some believe that oni can be spiritually placated through proper ritual worship that transforms them back into kami, many of these would-be saviors fall to oni's notorious brute strength, flesh-rending teeth, and command of storms.

Oni possess the ability to disguise themselves as other humanoids. They are rarely creative in their disguises, often choosing a specific appearance similar to their oni form and sticking with it. This simplicity catches many by surprise, however, as people assume oni are limited to a single alternate form, which is by no means the case.

```statblock
creature: "Caldera Oni"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
