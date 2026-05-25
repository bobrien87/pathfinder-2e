---
type: creature
group: ["Beast"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Chimera"
level: "8"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Beast"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+16; [[Darkvision]], [[Scent]] (imprecise) 30 feet"
languages: "Draconic"
skills:
  - name: Skills
    desc: "Acrobatics +14, Athletics +18, Stealth +18"
abilityMods: ["+6", "+2", "+4", "-3", "+2", "+0"]
abilities_top:
  - name: "Draconic Bite"
    desc: "A chimera's dragon head deals an extra 2d6 untyped damage of a type matching the damage dealt by its Dragon Breath."
armorclass:
  - name: AC
    desc: "27; **Fort** +18, **Ref** +16, **Will** +14"
health:
  - name: HP
    desc: "135"
abilities_mid:
  - name: "Multiple Reactions"
    desc: "A chimera gains 2 extra reactions each round that it can use only to make Reactive Strikes. It must use a different head for each reaction, and it can't use more than one on the same triggering action. If it loses one of its heads, it also loses one of these extra reactions."
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Three Headed"
    desc: "Any ability that would sever a chimera's head (such as a critical hit with a *Vorpal Weapon*) severs one head at random. Losing a head doesn't kill a chimera (as long as it has one head left), but it does prevent it from making Strikes with the lost head or using the head's Dragon Breath."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dragon Jaws +20 (`pf2:1`), **Damage** 2d6+9 piercing"
  - name: "Melee strike"
    desc: "Lion Jaws +20 (`pf2:1`), **Damage** 2d10+9 piercing"
  - name: "Melee strike"
    desc: "Goat Horns +20 (`pf2:1`), **Damage** 2d10+9 piercing"
  - name: "Melee strike"
    desc: "Claw +20 (`pf2:1`) (agile, unarmed), **Damage** 2d6+9 slashing"
spellcasting: []
abilities_bot:
  - name: "Dragon Breath"
    desc: "`pf2:2` The chimera breathes a cone or line that deals 9d6 damage to all creatures in the area (DC 26 basic save of a type indicated below). The chimera's dragon head is linked to one of the traditions of magic, which determines the area of its Dragon Breath, the type of damage it deals, and the type of save to avoid it. This ability gains the related traits. <br>  <br> The chimera can't use Dragon Breath again for 1d4 rounds. <br>  <br> - **Arcane** @Template[line|distance:60] of @Damage[9d6[force]|options:area-damage]{force} (DC 26 [[Reflex]] save) <br>  <br> - **Divine** @Template[line|distance:60] of @Damage[9d6[spirit]|options:area-damage]{spirit} (DC 26 [[Reflex]] save); this ability can also have the holy or unholy trait <br>  <br> - **Occult** @Template[cone|distance:30] of @Damage[9d6[mental]|options:area-damage]{mental} (DC 26 [[Will]] save) <br>  <br> - **Primal** @Template[cone|distance:30] of @Damage[9d6[acid]|options:area-damage]{acid}, @Damage[9d6[cold]|options:area-damage]{cold}, @Damage[9d6[electricity]|options:area-damage]{electricity}, @Damage[9d6[fire]|options:area-damage]{fire}, or @Damage[9d6[sonic]|options:area-damage]{sonic} (DC 26 [[Reflex]] save); or @Damage[9d6[poison]|options:area-damage]{poison} (DC 26 [[Fortitude]] save)"
  - name: "Three-Headed Strike"
    desc: "`pf2:2` The chimera makes a Strike with its dragon jaws, lion jaws, and goat horns, each at a -2 penalty and targeting a different creature. These Strikes count as only one attack for the chimera's multiple attack penalty, and the penalty doesn't increase until after it has made all three attacks."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The chimera is the archetypal example of an unnatural monster made up of a monstrous mix of wildly different component creatures: in this case, a lion, a dragon, and a goat. Wild, hateful, and hungry, it tries to eat any creature it sees, but sometimes a strong-willed master is able to compel a chimera to serve as a guardian or even a mount. If such an individual ever loses their control over the chimera, they are often the first to be devoured.

```statblock
creature: "Chimera"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
