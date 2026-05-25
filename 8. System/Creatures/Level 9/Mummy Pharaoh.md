---
type: creature
group: ["Mummy", "Undead"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Mummy Pharaoh"
level: "9"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Mummy"
trait_02: "Undead"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+20; [[Darkvision]]"
languages: "Necril (plus any two languages they knew while alive)"
skills:
  - name: Skills
    desc: "Deception +18, Intimidation +20, Occultism +15, Religion +20, Stealth +13"
abilityMods: ["+5", "+2", "+4", "+0", "+5", "+5"]
abilities_top: []
armorclass:
  - name: AC
    desc: "27; **Fort** +19, **Ref** +15, **Will** +20"
health:
  - name: HP
    desc: "175; sacred wrappings, void healing; **Immunities** death effects, disease, paralyzed, poison, unconscious, bleed; **Weaknesses** fire 10, water 10"
abilities_mid:
  - name: "+1 Status to All Saves vs. Vitality"
    desc: ""
  - name: "Reactive Strike (Special)"
    desc: "`pf2:r` The mummy pharaoh can use Reactive Strike when a creature within its reach uses a concentrate action, in addition to its normal trigger. It can disrupt triggering concentrate actions, and it disrupts actions on any hit, not just a critical hit. <br>  <br> **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Rejuvenation"
    desc: "When a mummy pharaoh is destroyed, necromantic energies rebuild its body in its tomb over 1d10 days. If the body is destroyed during that time, the process starts anew. A reforming mummy pharaoh is destroyed permanently if their tomb is consecrated."
  - name: "Sacred Wrappings"
    desc: "When a creature deals physical damage to the pharaoh or triggers one of the pharaoh's weaknesses, it must succeed at a DC 28 [[Will]] save or become [[Doomed]] 1. <br>  <br> Regardless of the results of the save, the creature is then immune to that mummy's sacred wrappings for 24 hours."
  - name: "Undead Mastery"
    desc: "100 feet. <br>  <br> Commanded or allied undead in the aura that have a lower level than the mummy pharaoh gain a +1 circumstance bonus to attack rolls, damage rolls, AC, saves, and skill checks. <br>  <br> > [!danger] Effect: Undead Mastery"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +20 (`pf2:1`) (agile, unarmed), **Damage** 1d6 void plus 1d10+11 bludgeoning"
  - name: "Melee strike"
    desc: "Longspear +21 (`pf2:1`) (magical, reach 10 ft.), **Damage** 1d6 void plus 2d8+11 piercing"
spellcasting: []
abilities_bot:
  - name: "Sandstorm Wrath"
    desc: "`pf2:2` The mummy pharaoh exhales a @Template[cone|distance:60] of superheated sand that deals @Damage[5d6[fire],5d6[slashing]|options:area-damage]{5d6 fire damage and 5d6 slashing damage} (DC 28 [[Reflex]] save). <br>  <br> The mummy pharaoh can't use Sandstorm Wrath again for 1d4 rounds."
  - name: "Veil of Sand"
    desc: "`pf2:1` Sand whirls around the mummy pharaoh in a 5-foot emanation until the beginning of their next turn. Creatures inside the sand are [[Concealed]] to those outside it and any living creature ending its turn within the sand takes @Damage[4d6[slashing]|options:area-damage] damage with a DC 28 [[Fortitude]] save <br>  <br> Veil of Sand ends if the mummy takes damage from their water weakness."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

While mummy guardians are undead crafted from the corpses of sacrificed—usually unwilling victims—and retain only fragments of their memories, a mummy pharaoh is the result of a deliberate embrace of undeath by a sadistic and cruel ruler. The transformation from life to undeath beneath the scorching desert sand is only somewhat less awful, but as the transition is an intentional bid to escape death by a powerful personality who fully embraces the blasphemous repercussions of the choice, the mummy pharaoh retains its memories and personality intact.

While many cultures practice mummification for benign reasons, undead mummies are created through grueling rituals, typically to provide eternally vigilant guardians. Much more rarely, a body mummified without those special rites can rise again due to its hatred of the living.

```statblock
creature: "Mummy Pharaoh"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
