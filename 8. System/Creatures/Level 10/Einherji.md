---
type: creature
group: ["Aesir", "Monitor"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Einherji"
level: "10"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Aesir"
trait_02: "Monitor"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+17; [[Darkvision]]"
languages: "Common, Hallit, Jotun"
skills:
  - name: Skills
    desc: "Athletics +25, Crafting +16, Intimidation +21"
abilityMods: ["+7", "+4", "+6", "+0", "+1", "+3"]
abilities_top:
  - name: "Jotun Slayer"
    desc: "The einherji has a +4 circumstance bonus to damage rolls made against giants and creatures that are at least two sizes larger than the einherji."
armorclass:
  - name: AC
    desc: "30; **Fort** +22, **Ref** +18, **Will** +17"
health:
  - name: HP
    desc: "175; **Resistances** piercing 10"
abilities_mid:
  - name: "+4 to Will Saves vs. Fear"
    desc: ""
  - name: "Raise a Shield"
    desc: "`pf2:1` **Requirements** You are wielding a shield. <br>  <br> You position your shield to protect yourself. When you have Raised a Shield, you gain its listed circumstance bonus to AC. Your shield remains raised until the start of your next turn."
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within your reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> You lash out at a foe that leaves an opening. Make a melee Strike against the triggering creature. If your attack is a critical hit and the trigger was a manipulate action, you disrupt that action. This Strike doesn't count toward your multiple attack penalty, and your multiple attack penalty doesn't apply to this Strike."
  - name: "Shield Block"
    desc: "`pf2:r` **Trigger** The monster has its shield raised and takes damage from a physical attack. <br>  <br> **Effect** The monster snaps its shield into place to deflect a blow. The shield prevents the monster from taking an amount of damage up to the shield's Hardness. The monster and the shield each take any remaining damage, possibly breaking or destroying the shield."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Longsword +23 (`pf2:1`) (versatile p), **Damage** 2d8+13 slashing"
  - name: "Melee strike"
    desc: "Fist +22 (`pf2:1`) (agile, unarmed), **Damage** 2d6+13 bludgeoning"
  - name: "Melee strike"
    desc: "Dagger +23 (`pf2:1`) (agile, versatile s), **Damage** 2d4+13 piercing"
  - name: "Melee strike"
    desc: "Dagger +20 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 2d4+13 piercing"
spellcasting:
  - name: "Champion Devotion Spells"
    desc: "DC 29, attack +21<br>**5th** [[Spectral Advance]]"
abilities_bot:
  - name: "Challenge Foe"
    desc: "`pf2:1` The einherji challenges one creature they can see to single combat, attempting to [[Demoralize]] that target. <br>  <br> This target remains the einherji's foe until it's defeated, it flees, or the encounter ends. The einherji gains a circumstance bonus to damage equal to their number of weapon damage dice against their designated foe but takes an equivalent circumstance penalty to damage against any other creature. <br>  <br> If the einherji is defeated by their challenged foe, the shame causes them to lose use of their champion devotion spells for 1 week or until they challenge the same foe again and emerge victorious, whichever comes first."
  - name: "Instant Repair"
    desc: "`pf2:1` The einherji [[Repairs]] their shield. They can't use this ability if the shield is completely destroyed."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Einherjar are mighty warriors chosen by valkyries from the ranks of those slain in terrible and legendary battles. Forged from the souls of the greatest warriors, the implacable einherjar serve as the foot soldiers of pantheons, skilled in handto-hand combat and slaying giants.

Einherjar often come from warrior cultures, including Ulfen vikings (like the einherji represented in this entry), particularly fierce pirates from the Shackles, and even Osirian conquerors. They can be chosen from wherever war and might hold sway; many deities who hold the call of battle and the pursuit of physical power more sacred than concepts of good and evil might count einherjar warriors and valkyrie choosers of the slain among their chosen servitors. For example, Gorum, Besmara, and Sekhmet have all elevated fallen worshippers as einherjar. Einherjar dedicated to different deities often wield weapons or possess varying cosmetic appearances based on their deity's preferred weapon and their place of death; however, they're universally stalwart, implacable, and efficiently deadly. Einherjar with two-handed weapons or who arise from other backgrounds often have different abilities in place of Jotun Slayer and Instant Repair.

```statblock
creature: "Einherji"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
