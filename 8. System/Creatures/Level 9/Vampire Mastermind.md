---
type: creature
group: ["Undead", "Unholy"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Vampire Mastermind"
level: "9"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Undead"
trait_02: "Unholy"
trait_03: "Vampire"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+20; [[Darkvision]]"
languages: "Common, Necril (plus one regional language)"
skills:
  - name: Skills
    desc: "Acrobatics +17, Arcana +21, Athletics +18, Deception +20, Diplomacy +20, Intimidation +22, Society +19, Stealth +19"
abilityMods: ["+3", "+4", "+1", "+6", "+4", "+5"]
abilities_top:
  - name: "Children of the Night"
    desc: "The vampire's presence brings forth creatures of the night to do the master's bidding. These typically include Rat Swarms, Bat Swarms, and Wolves, but can include other creatures. <br>  <br> The vampire can give telepathic orders to these creatures as long as they are within 100 feet, but they can't communicate back."
  - name: "Create Servitor"
    desc: "If a creature dies after being reduced to 0 HP by Drink Blood, the vampire can turn this victim into a vampire servitor by donating some of their own blood to the victim and burying the victim in earth for 3 nights. <br>  <br> A vampiric servitor is compelled to obey its creator, but if a vampire controls too many vampiric servitors at once (as determined by the GM), or if the servitor is a higher level than the vampire that created it, strongwilled servitors can free themselves by succeeding at a [[Will]] save saving throw against the vampire's Will DC."
  - name: "Steady Spellcasting"
    desc: "If another creature's reaction would disrupt the vampire mastermind's spellcasting action, the vampire attempts a DC 15 flat check. If the vampire succeeds, their action isn't disrupted."
armorclass:
  - name: AC
    desc: "27; **Fort** +15, **Ref** +18, **Will** +20"
health:
  - name: HP
    desc: "115; coffin restoration, fast healing 10, void healing; **Immunities** death effects, disease, paralyzed, poison, sleep"
abilities_mid:
  - name: "Fast Healing 10"
    desc: "A monster with this ability regains the given number of Hit Points each round at the beginning of its turn."
  - name: "Coffin Restoration"
    desc: "Unlike other undead, a vampire isn't destroyed at 0 HP. Instead, it falls [[Unconscious]]. If its body rests in its coffin for 1 hour, the vampire gains 1 HP, after which its fast healing begins to function normally."
  - name: "Mist Escape"
    desc: "`pf2:0` **Trigger** The vampire is reduced to 0 HP. <br>  <br> **Effect** The vampire uses Turn to Mist. They can take move actions to move toward its coffin even though it's at 0 HP. While at 0 HP in this form, the vampire is unaffected by further damage. <br>  <br> They automatically returns to its corporeal form, unconscious, if they reaches their coffin or after 2 hours, whichever comes first."
  - name: "Vampire Vulnerabilities"
    desc: "All vampires possess the following vulnerabilities. <br>  <br> - **Compulsions** Vampires are creatures with strange and unknowable compulsions. A typical vampire can't voluntarily cross running water unless they're transported while they hide within their coffin, nor can they enter a private dwelling unless invited in by someone with the authority to do so. At your discretion, vampires might have different compulsions—a pirate vampire might not be able to set foot on solid ground without being invited, for example. The vampire can still be forced to do these things and might be able to overcome their compulsion just as they do their revulsion. <br>  <br> - **Revulsion** A vampire can't voluntarily come within 10 feet of brandished garlic or a brandished religious symbol of a deity with a holy sanctification option. To brandish garlic or a religious symbol, a creature must Interact to do so, and it remains brandished for 1 round (similar to Raising a Shield). If the vampire involuntarily comes within 10 feet of an object of their revulsion, they gain the [[Fleeing]] condition, running from the object of their revulsion until they end an action beyond 10 feet. After 1 round of being exposed to the subject of their revulsion, a vampire can attempt a DC 25 [[Will]] save as a single action, which has the concentrate trait. On a success, they overcome their revulsions for 1d6 rounds (or 1 hour on a critical success). <br>  <br> - **Stake** A wooden stake driven through a vampire's heart drops the vampire to 0 HP and prevents them from healing above 0 HP, even in their coffin. Staking a vampire requires 3 actions and works only if the vampire is [[Unconscious]]. If the stake is removed, the vampire can heal above 0 HP again, and if they're in their coffin, the 1-hour rest period begins once the stake is removed. If the vampire's head is severed and anointed with holy water while the stake is in place, the vampire is destroyed. <br>  <br> - **Sunlight** If exposed to direct sunlight, a vampire immediately becomes [[Slowed]] 1. The slowed value increases by 1 each time the vampire ends their turn in sunlight, and the condition ends when they're no longer in sunlight. If the vampire loses all their actions in this way, they're destroyed. Due to their supernatural aversion to light, vampires don't cast shadows or show a reflection in mirrors"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +18 (`pf2:1`) (agile, unarmed), **Damage** 2d8+9 slashing plus [[Grab]]"
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 29, attack +19<br>**4th** (4 slots) [[Fire Shield]], [[Illusory Disguise]], [[Vision of Death]], [[Wall of Fire]]<br>**3rd** (4 slots) [[Dispel Magic]], [[Fireball]], [[Haste]], [[Lightning Bolt]]<br>**2nd** (4 slots) [[Blur]], [[Floating Flame]], [[Invisibility]], [[Stupefy]]<br>**1st** (4 slots) [[Dizzying Colors]], [[Dizzying Colors]], [[Enfeeble]], [[Fleet Step]]<br>**Cantrips** [[Detect Magic]], [[Frostbite]], [[Message]], [[Telekinetic Hand]], [[Sigil]]"
  - name: "Divine Innate Spells"
    desc: "DC 26, attack +18<br>**6th** [[Dominate (At Will) (See Dominate)]]"
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` The vampire transforms into one of its animal forms or back into its normal form. Most vampires can turn into a bat, but some can turn into a different creature, such as a rat or a wolf. <br>  <br> - **Giant Bat** <br>  <br> - **Senses** echolocation 40 feet, <br>  <br> - **Speed** 20 feet, fly 30 feet, <br>  <br> - **Melee** fangs +19 **Damage** 2d8+9 piercing <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Dominate"
    desc: "`pf2:2` The vampire can cast [[Dominate]] at will as a divine innate spell. Casting it requires staring into the target's eyes, giving the spell the visual trait (DC 26 [[Will]] save). A creature that succeeds is temporarily immune to that vampire's Dominate for 24 hours. <br>  <br> Fully destroying the vampire ends the domination, but merely reducing the vampire to 0 HP is insufficient to break the spell."
  - name: "Drain Bonded Item"
    desc: "`pf2:0` **Frequency** once per day <br>  <br> **Requirements** The vampire mastermind hasn't acted yet on this turn <br>  <br> **Effect** The vampire expends the power stored in their signet ring. This gives the vampire the ability to cast one prepared spell they had already previously cast today without spending a spell slot. The vampire must still Cast the Spell and meet the spell's other requirements."
  - name: "Drink Blood"
    desc: "`pf2:1` **Requirement** A [[Grabbed]], [[Paralyzed]], [[Restrained]], [[Unconscious]], or willing creature is within the vampire's reach. <br>  <br> **Effect** The vampire sinks its fangs into that creature to drink its blood. This requires an [[Athletics]] check against the victim's Fortitude DC if the victim is grabbed and is automatic for any of the other conditions. <br>  <br> The victim is [[Drained]] 2 and the vampire regains 10 HP, gaining any excess HP as temporary Hit Points. Drinking Blood from a creature that's already drained doesn't restore any HP to the vampire but increases the victim's drained value by 1, killing the victim when it reaches drained 5. A vampire can also consume blood that's been emptied into a vessel for sustenance, but it gains no HP from doing so. <br>  <br> A victim's drained condition decreases by 1 per week. A blood transfusion, which requires a DC 20 [[Medicine]] check and sufficient blood or a blood donor, reduces the drain by 1 after 10 minutes."
  - name: "Turn to Mist"
    desc: "`pf2:1` The vampire turns into a cloud of vapor, as the [[Vapor Form]] spell, or back to its normal form. The vampire loses fast healing while in gaseous form. <br>  <br> The vampire can remain in this form indefinitely."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Vampire masterminds are evil wizards who control entire cabals of the undead and instill fear in the hearts of mortals far and wide.

Vampires are undead creatures that feed on the blood of the living.

```statblock
creature: "Vampire Mastermind"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
